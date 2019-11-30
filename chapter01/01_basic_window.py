"""
    Boiler plate code for every PySide2 based Maya Application UI
"""
from PySide2 import QtWidgets
from PySide2 import QtCore
from shiboken2 import wrapInstance
from maya import _OpenMayaUI as omui


def maya_main_window():
    """
    :returns Maya main window widget as Python object
    """
    main_window_ptr = omui.MQtUtil_mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class TestDialog(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(TestDialog, self).__init__(parent)
        self.setWindowTitle("Test Dialog")
        self.setMinimumWidth(300)
        self.setMinimumHeight(200)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        pass

    def create_layout(self):
        pass


if __name__ == '__main__':
    dialog = TestDialog()
    dialog.show()
