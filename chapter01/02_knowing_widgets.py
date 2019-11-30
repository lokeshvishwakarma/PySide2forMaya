"""
    Introduction to most commonly used widgets from PySide2
    1. QLabel
    2. QLineEdit
    3. QCheckBox
    4. QPushButton
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
        self.setWindowTitle('Test Dialog')
        self.setMinimumWidth(300)
        self.setMinimumHeight(200)
        # Below Line removes the help button on the top right corner of the dialog and this is "Windows" specific
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        """
        Create all the widgets required for the tool here
        :return: None
        """
        self.name_lbl = QtWidgets.QLabel('Name: ')
        self.name_le = QtWidgets.QLineEdit()
        self.all_chb = QtWidgets.QCheckBox('All')
        self.selected_chb = QtWidgets.QCheckBox('Selected')
        self.hidden_chb = QtWidgets.QCheckBox('Hidden')
        self.locked_chb = QtWidgets.QCheckBox('Locked')
        self.run_btn = QtWidgets.QPushButton('Run')

    def create_layout(self):
        """
        Create layouts for the tool and put all the widgets in those layouts
        :return: None
        """
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)  # This sets the main_layout

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addWidget(self.name_lbl)
        h_box1.addWidget(self.name_le)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.all_chb)
        h_box2.addWidget(self.selected_chb)
        h_box2.addWidget(self.hidden_chb)
        h_box2.addWidget(self.locked_chb)

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addWidget(self.run_btn)

        main_layout.addLayout(h_box1)
        main_layout.addLayout(h_box2)
        main_layout.addLayout(h_box3)


if __name__ == '__main__':
    dialog = TestDialog()
    dialog.show()
