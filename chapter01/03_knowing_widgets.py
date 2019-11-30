"""
    Introduction to most commonly used widgets from PySide2
    1. QComboBox
    2. QRadioButton
    3. QSpinBox
    4. QTextEdit
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
        self.item_cmb = QtWidgets.QComboBox()
        self.item_cmb.addItems(['item1', 'item2', 'item3', 'item4'])
        self.one_rad = QtWidgets.QRadioButton('One')
        self.two_rad = QtWidgets.QRadioButton('Two')
        self.three_rad = QtWidgets.QRadioButton('Three')
        self.four_rad = QtWidgets.QRadioButton('Four')
        self.count_spbox = QtWidgets.QSpinBox()
        self.read_textedit = QtWidgets.QTextEdit()
        self.read_textedit.setPlaceholderText('Type your text here.')

    def create_layout(self):
        """
        Create layouts for the tool and put all the widgets in those layouts
        :return: None
        """
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addWidget(self.item_cmb)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.one_rad)
        h_box2.addWidget(self.two_rad)
        h_box2.addWidget(self.three_rad)
        h_box2.addWidget(self.four_rad)
        h_box2.addWidget(self.count_spbox)

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addWidget(self.read_textedit)

        # Add all other layouts to main layout
        main_layout.addLayout(h_box1)
        main_layout.addLayout(h_box2)
        main_layout.addLayout(h_box3)


if __name__ == '__main__':
    dialog = TestDialog()
    dialog.show()
