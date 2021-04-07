from pythonforandroid.recipe import IncludedFilesBehaviour, CppCompiledComponentsPythonRecipe


class OctoBotRecipe(IncludedFilesBehaviour, CppCompiledComponentsPythonRecipe):
    # version = 'master'
    name = "OctoBot"
    # url = 'https://github.com/Drakkar-Software/OctoBot/archive/{version}.zip'

    # A list of any other recipe names that must be built before this one
    depends = ['numpy', 'setuptools', 'cython']

    python_depends = ['OctoBot==0.4.0b7']

    call_hostpython_via_targetpython = False
    install_in_hostpython = False


recipe = OctoBotRecipe()
