import sys

from PySide2 import QtWidgets


from PyGraph import initialize
from PyGraph.main_window import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)

    initialize()

    instance = MainWindow().instance(software="standalone")
    if instance is not None:
        instance.activateWindow()
        instance.show()

        try:
            sys.exit(app.exec_())
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
