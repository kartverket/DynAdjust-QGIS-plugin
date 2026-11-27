# -*- coding: utf-8 -*-
"""
/***************************************************************************
 dynadjustpluginDialog
                                 A QGIS plugin
 Description
                             -------------------
        copyright            : (C) 2026 by Sveinung Himle
        email                : sveinung.himle@kartverket.no
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from xsdata.exceptions import ParserError

from dynadjustplugin.models.dnaproj_parser import convert_dnaproj_to_xml
from dynadjustplugin.settings_dialog import SettingsDialog

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'dynadjustplugin_dialog_base.ui'))


class dynadjustpluginDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(dynadjustpluginDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        dialog_layout = QtWidgets.QVBoxLayout(self)
        dialog_layout.setContentsMargins(0, 0, 0, 0)
        dialog_layout.addWidget(self.widget)

        file_row = QtWidgets.QHBoxLayout(self.widget)
        file_row.setContentsMargins(20, 10, 17, 0)
        file_row.setSpacing(0)
        self.label.setFixedWidth(141)
        self.textEdit.setFixedHeight(31)
        self.toolButton.setFixedSize(41, 31)
        file_row.addWidget(self.label)
        file_row.addSpacing(19)
        file_row.addWidget(self.textEdit, 1)
        file_row.addSpacing(9)
        file_row.addWidget(self.toolButton)

        self.toolButton.clicked.connect(self.select_dna_project_file)
        self.active_project_xml = None
        self.settings_dialog = SettingsDialog(self)
        self.settingsButton.clicked.connect(self.show_settings_dialog)

    def show_settings_dialog(self):
        if self.active_project_xml is None:
            QtWidgets.QMessageBox.warning(
                self,
                self.tr("No project selected"),
                self.tr("Select a DNA project file first."),
            )
            return

        try:
            self.settings_dialog.load_project_xml(self.active_project_xml)
        except (OSError, ParserError, ValueError) as error:
            QtWidgets.QMessageBox.critical(
                self,
                self.tr("Unable to load project settings"),
                str(error),
            )
            return

        self.settings_dialog.show()
        self.settings_dialog.raise_()
        self.settings_dialog.activateWindow()

    def select_dna_project_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            self.tr("Select DNA project file"),
            "",
            self.tr("DNA project files (*.dnaproj)"),
        )
        if file_path:
            self.textEdit.setPlainText(file_path)
            self.active_project_xml = None
            try:
                output_path = convert_dnaproj_to_xml(file_path)
            except (OSError, ValueError) as error:
                QtWidgets.QMessageBox.critical(
                    self,
                    self.tr("Project conversion failed"),
                    str(error),
                )
                return

            self.active_project_xml = output_path
            QtWidgets.QMessageBox.information(
                self,
                self.tr("Project converted"),
                self.tr("XML file created at:\n{}").format(output_path),
            )
