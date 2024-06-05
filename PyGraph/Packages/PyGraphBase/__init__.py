from collections import OrderedDict

from PyGraph.Packages.PyGraphBase.Tools.CompileTool import CompileTool


_TOOLS = OrderedDict()
_TOOLS[CompileTool.__name__] = CompileTool


class PyGraphBase(object):
    def __init__(self):
        super().__init__()

    @staticmethod
    def GetToolClasses():
        return _TOOLS
