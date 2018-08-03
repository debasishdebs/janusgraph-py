# Name: Debasish Kanhar
# Emp ID: 05222V


from pybuilder.core import use_plugin, init

use_plugin("python.core")
# the python unittest plugin allows running python's standard library unittests
use_plugin("python.unittest")
# this plugin allows installing project dependencies with pip
use_plugin("python.install_dependencies")
# a plugin that measures unit test statement coverage
use_plugin("python.coverage")
# for packaging purposes since we'll build a tarball
use_plugin("python.distutils")

name = "janusgraph-python"

version = "0.0.1"

default_task = ['install_dependencies', 'publish']

# This is an initializer, a block of logic that runs before the project is built.
@init
def initialize(project):
    # Nothing happens here yet, but notice the `project` argument which is automatically injected.
    project.set_property("coverage_break_build", False)  # default is True
    project.depends_on("gremlinpython", "==3.3")
    pass
