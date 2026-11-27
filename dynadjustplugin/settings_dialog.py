import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from xsdata.formats.dataclass.parsers import XmlParser

from dynadjustplugin.models import DnaProject

SETTINGS_FORM_CLASS, _ = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), "settings_dialog.ui")
)


class SettingsDialog(QtWidgets.QDialog, SETTINGS_FORM_CLASS):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.setupUi(self)

        self.scroll_area = QtWidgets.QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.formLayoutWidget)

        dialog_layout = QtWidgets.QVBoxLayout(self)
        dialog_layout.setContentsMargins(0, 0, 0, 0)
        dialog_layout.addWidget(self.scroll_area)

    def load_project_xml(self, xml_file):
        project = XmlParser().parse(str(xml_file), DnaProject)

        while self.formLayout.rowCount():
            self.formLayout.removeRow(0)

        for section in project.section:
            section_label = QtWidgets.QLabel(section.name)
            section_label.setStyleSheet("font-weight: bold;")
            self.formLayout.addRow(section_label)

            for setting in section.setting:
                value_field = QtWidgets.QLineEdit(setting.value or "")
                value_field.setReadOnly(True)
                value_field.setToolTip(setting.value or "")
                self.formLayout.addRow(setting.name, value_field)

        self.setWindowTitle("Project settings - {}".format(project.source))