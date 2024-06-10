import os
import pkgutil


from PyGraph import Packages

__PACKAGES = {}
__PACKAGE_PATHS = {}
__HASHABLE_TYPES = []

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
RESOURCES_ICONS = os.path.join(PROJECT_ROOT, "PyGraph", "resources", "icons")


def initialize(additionalPackageLocations=None, software=""):
    if additionalPackageLocations is None:
        additionalPackageLocations = []

    packagePaths = Packages.__path__
    # ['D:\\Works\\studio\\maya_pipeline\\graph_builder\\PyGraph\\Packages']

    for importer, modName, isPkg in pkgutil.iter_modules(packagePaths):
        print(f"{modName=}, {isPkg=}")
        try:
            if isPkg:
                mod = importer.find_spec(modName).loader.load_module()
                package = getattr(mod, modName)()
                __PACKAGES[modName] = package
                __PACKAGE_PATHS[modName] = os.path.normpath(mod.__path__[0])
        except Exception as e:
            print(f"Fatal error: Error on Module {modName} : {str(e)}")
            continue
