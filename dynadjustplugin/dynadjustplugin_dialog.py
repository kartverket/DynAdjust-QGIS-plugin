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

    def select_dna_project_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            self.tr("Select DNA project file"),
            "",
            self.tr("DNA project files (*.dnaproj)"),
        )
        if file_path:
            self.textEdit.setPlainText(file_path)
