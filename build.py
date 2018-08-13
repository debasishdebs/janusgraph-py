# Name: Debasish Kanhar


from pybuilder.core import use_plugin, init, Author

authors = [Author("Debasish Kanhar", "dekanhar@in.ibm.com")]
description = "Python client drivers for JanusGraph"
license = "Apache License v2.0"

name = "janusgraph_python"

tinkerpop_version = "3.3.3"
janusgraph_version = "0.3.0"
version = "0.0.2"

use_plugin("python.core")
# the python unittest plugin allows running python's standard library unittests
use_plugin("python.unittest")
# this plugin allows installing project dependencies with pip
use_plugin("python.install_dependencies")
# a plugin that measures unit test statement coverage
use_plugin("python.coverage")
# for packaging purposes since we'll build a tarball
use_plugin("python.distutils")

default_task = ['clean', 'install_dependencies', 'publish']

# This is an initializer, a block of logic that runs before the project is built.
@init
def initialize(project):
    # Nothing happens here yet, but notice the `project` argument which is automatically injected.
    project.set_property("coverage_break_build", False)  # default is True
    project.set_property("dir_dist", "target/dist/" + project.name)
    project.depends_on("gremlinpython", "=={}".format(tinkerpop_version))
    pass
