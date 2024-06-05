import sys

from qtpy import QtWidgets

from PyGraph.graph_builder import GraphBuilder


def main():
    app = QtWidgets.QApplication(sys.argv)

    wnd = GraphBuilder()
    wnd.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
