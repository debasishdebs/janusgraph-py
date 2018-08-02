/*
 *  Licensed to the Apache Software Foundation (ASF) under one
 *  or more contributor license agreements.  See the NOTICE file
 *  distributed with this work for additional information
 *  regarding copyright ownership.  The ASF licenses this file
 *  to you under the Apache License, Version 2.0 (the
 *  "License"); you may not use this file except in compliance
 *  with the License.  You may obtain a copy of the License at
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing,
 *  software distributed under the License is distributed on an
 *  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 *  KIND, either express or implied.  See the License for the
 *  specific language governing permissions and limitations
 *  under the License.
 */

package org.apache.tinkerpop.gremlin.python.jsr223;

import org.apache.commons.configuration.ConfigurationConverter;
import org.apache.tinkerpop.gremlin.process.traversal.Bytecode;
import org.apache.tinkerpop.gremlin.process.traversal.Operator;
import org.apache.tinkerpop.gremlin.process.traversal.P;
import org.apache.tinkerpop.gremlin.process.traversal.SackFunctions;
import org.apache.tinkerpop.gremlin.process.traversal.Translator;
import org.apache.tinkerpop.gremlin.process.traversal.Traversal;
import org.apache.tinkerpop.gremlin.process.traversal.TraversalStrategy;
import org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.GraphTraversal;
import org.apache.tinkerpop.gremlin.process.traversal.step.TraversalOptionParent;
import org.apache.tinkerpop.gremlin.process.traversal.strategy.TraversalStrategyProxy;
import org.apache.tinkerpop.gremlin.process.traversal.util.ConnectiveP;
import org.apache.tinkerpop.gremlin.process.traversal.util.OrP;
import org.apache.tinkerpop.gremlin.structure.Edge;
import org.apache.tinkerpop.gremlin.structure.Element;
import org.apache.tinkerpop.gremlin.structure.T;
import org.apache.tinkerpop.gremlin.structure.Vertex;
import org.apache.tinkerpop.gremlin.structure.VertexProperty;
import org.apache.tinkerpop.gremlin.structure.util.StringFactory;
import org.apache.tinkerpop.gremlin.util.function.Lambda;
import org.apache.tinkerpop.gremlin.util.iterator.ArrayIterator;
import org.apache.tinkerpop.gremlin.util.iterator.IteratorUtils;

import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * @author Marko A. Rodriguez (http://markorodriguez.com)
 * @author Stephen Mallette (http://stephen.genoprime.com)
 */
public class PythonTranslator implements Translator.ScriptTranslator {

    private static final Set<String> STEP_NAMES = Stream.of(GraphTraversal.class.getMethods()).filter(method -> Traversal.class.isAssignableFrom(method.getReturnType())).map(Method::getName).collect(Collectors.toSet());
    private static final Set<String> NO_STATIC = Stream.of(T.values(), Operator.values())
            .flatMap(arg -> IteratorUtils.stream(new ArrayIterator<>(arg)))
            .map(arg -> ((Enum) arg).name())
            .collect(Collectors.toCollection(() -> new HashSet<>(Collections.singleton("not"))));

    private final String traversalSource;
    private final boolean importStatics;

    PythonTranslator(final String traversalSource, final boolean importStatics) {
        this.traversalSource = traversalSource;
        this.importStatics = importStatics;
    }

    public static PythonTranslator of(final String traversalSource, final boolean importStatics) {
        return new PythonTranslator(traversalSource, importStatics);
    }

    public static PythonTranslator of(final String traversalSource) {
        return new PythonTranslator(traversalSource, false);
    }

    @Override
    public String getTraversalSource() {
        return this.traversalSource;
    }

    @Override
    public String translate(final Bytecode bytecode) {
        return this.internalTranslate(this.traversalSource, bytecode);
    }

    @Override
    public String getTargetLanguage() {
        return "gremlin-python";
    }

    @Override
    public String toString() {
        return StringFactory.translatorString(this);
    }

    ///////

    private String internalTranslate(final String start, final Bytecode bytecode) {
        final StringBuilder traversalScript = new StringBuilder(start);
        for (final Bytecode.Instruction instruction : bytecode.getInstructions()) {
            final String methodName = instruction.getOperator();
            final Object[] arguments = instruction.getArguments();
            if (0 == arguments.length)
                traversalScript.append(".").append(resolveSymbol(methodName)).append("()");
            else if (methodName.equals("range") && 2 == arguments.length)
                if (((Number) arguments[0]).longValue() + 1 == ((Number) arguments[1]).longValue())
                    traversalScript.append("[").append(arguments[0]).append("]");
                else
                    traversalScript.append("[").append(arguments[0]).append(":").append(arguments[1]).append("]");
            else if (methodName.equals("limit") && 1 == arguments.length)
                traversalScript.append("[0:").append(arguments[0]).append("]");
            else if (methodName.equals("values") && 1 == arguments.length && traversalScript.length() > 3 && !STEP_NAMES.contains(arguments[0].toString()))
                traversalScript.append(".").append(arguments[0]);
            else {
                traversalScript.append(".");
                String temp = resolveSymbol(methodName) + "(";
                for (final Object object : arguments) {
                    temp = temp + convertToString(object) + ",";
                }
                traversalScript.append(temp.substring(0, temp.length() - 1)).append(")");
            }
            // clip off __.
            if (this.importStatics && traversalScript.substring(0, 3).startsWith("__.")
                    && !NO_STATIC.stream().filter(name -> traversalScript.substring(3).startsWith(resolveSymbol(name))).findAny().isPresent()) {
                traversalScript.delete(0, 3);
            }
        }
        return traversalScript.toString();
    }

    protected String convertToString(final Object object) {
        if (object instanceof Bytecode.Binding)
            return ((Bytecode.Binding) object).variable();
        else if (object instanceof Bytecode)
            return this.internalTranslate("__", (Bytecode) object);
        else if (object instanceof Traversal)
            return convertToString(((Traversal) object).asAdmin().getBytecode());
        else if (object instanceof String)
            return ((String) object).contains("\"") ? "\"\"\"" + object + "\"\"\"" : "\"" + object + "\"";
        else if (object instanceof Set) {
            final Set<String> set = new LinkedHashSet<>(((Set) object).size());
            for (final Object item : (Set) object) {
                set.add(convertToString(item));
            }
            return "set(" + set.toString() + ")";
        } else if (object instanceof List) {
            final List<String> list = new ArrayList<>(((List) object).size());
            for (final Object item : (List) object) {
                list.add(convertToString(item));
            }
            return list.toString();
        } else if (object instanceof Map) {
            final StringBuilder map = new StringBuilder("{");
            for (final Map.Entry<?, ?> entry : ((Map<?, ?>) object).entrySet()) {
                map.append(convertToString(entry.getKey())).
                        append(":").
                        append(convertToString(entry.getValue())).
                        append(",");
            }
            return map.length() > 1 ? map.substring(0, map.length() - 1) + "}" : map.append("}").toString();
        } else if (object instanceof Long)
            return object + "L";
        else if (object instanceof TraversalStrategyProxy) {
            return resolveTraversalStrategyProxy((TraversalStrategyProxy) object);
        } else if (object instanceof TraversalStrategy) {
            return convertToString(new TraversalStrategyProxy((TraversalStrategy) object));
        } else if (object instanceof Boolean)
            return object.equals(Boolean.TRUE) ? "True" : "False";
        else if (object instanceof Class)
            return ((Class) object).getCanonicalName();
        else if (object instanceof VertexProperty.Cardinality)
            return "Cardinality." + resolveSymbol(object.toString());
        else if (object instanceof SackFunctions.Barrier)
            return "Barrier." + resolveSymbol(object.toString());
        else if (object instanceof TraversalOptionParent.Pick)
            return "Pick." + resolveSymbol(object.toString());
        else if (object instanceof Enum)
            return convertStatic(((Enum) object).getDeclaringClass().getSimpleName() + ".") + resolveSymbol(object.toString());
        else if (object instanceof P)
            return convertPToString((P) object, new StringBuilder()).toString();
        else if (object instanceof Element) {
            if (object instanceof Vertex) {
                final Vertex vertex = (Vertex) object;
                return "Vertex(" + convertToString(vertex.id()) + "," + convertToString(vertex.label()) + ")";
            } else if (object instanceof Edge) {
                final Edge edge = (Edge) object;
                return "Edge(" + convertToString(edge.id()) + "," +
                        convertToString(edge.outVertex()) + "," +
                        convertToString(edge.label()) + "," +
                        convertToString(edge.inVertex()) + ")";
            } else {
                final VertexProperty vertexProperty = (VertexProperty) object;
                return "VertexProperty(" + convertToString(vertexProperty.id()) + "," +
                        convertToString(vertexProperty.label()) + "," +
                        convertToString(vertexProperty.value()) + ")";
            }
        } else if (object instanceof Lambda)
            return convertLambdaToString((Lambda) object);
        else
            return null == object ? "None" : object.toString();
    }

    private String convertStatic(final String name) {
        return this.importStatics ? "" : name;
    }

    private StringBuilder convertPToString(final P p, final StringBuilder current) {
        if (p instanceof ConnectiveP) {
            final List<P<?>> list = ((ConnectiveP) p).getPredicates();
            for (int i = 0; i < list.size(); i++) {
                convertPToString(list.get(i), current);
                if (i < list.size() - 1)
                    current.append(p instanceof OrP ? ".or_(" : ".and_(");
            }
            current.append(")");
        } else
            current.append(convertStatic("P.")).append(p.getBiPredicate().toString()).append("(").append(convertToString(p.getValue())).append(")");
        return current;
    }

    protected String convertLambdaToString(final Lambda lambda) {
        final String lambdaString = lambda.getLambdaScript().trim();
        return lambdaString.startsWith("lambda") ? lambdaString : "lambda " + lambdaString;
    }

    protected String resolveSymbol(final String methodName) {
        return SymbolHelper.toPython(methodName);
    }

    protected String resolveTraversalStrategyProxy(final TraversalStrategyProxy proxy) {
        if (proxy.getConfiguration().isEmpty())
            return "TraversalStrategy(\"" + proxy.getStrategyClass().getSimpleName() + "\")";
        else
            return "TraversalStrategy(\"" + proxy.getStrategyClass().getSimpleName() + "\"," + convertToString(ConfigurationConverter.getMap(proxy.getConfiguration())) + ")";
    }
}
