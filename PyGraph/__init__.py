import sys
from PyGraph import Packages

try:
    sys.path.append("D:\\Works\\studio\\maya_pipeline\\graph_builder")
except Exception:
    pass


def initialize(additionalPackageLocations=None, software=""):
    if additionalPackageLocations is None:
        additionalPackageLocations = []

    packagePaths = Packages.__path__

if __name__ == "__main__":
    initialize()
