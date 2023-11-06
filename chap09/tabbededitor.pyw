#!/usr/bin/env python3
# Copyright (c) 2008-10 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import textedit
import qrc_resources


__version__ = "1.0.0"


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.tabWidget = QTabWidget()
        self.setCentralWidget(self.tabWidget)

        fileNewAction = self.createAction("&New", self.fileNew,
                QKeySequence.New, "filenew", "Create a text file")
        fileOpenAction = self.createAction("&Open...", self.fileOpen,
                QKeySequence.Open, "fileopen",
                "Open an existing text file")
        fileSaveAction = self.createAction("&Save", self.fileSave,
                QKeySequence.Save, "filesave", "Save the text")
        fileSaveAsAction = self.createAction("Save &As...",
                self.fileSaveAs, icon="filesaveas",
                tip="Save the text using a new filename")
        fileSaveAllAction = self.createAction("Save A&ll",
                self.fileSaveAll, icon="filesave",
                tip="Save all the files")
        fileCloseTabAction = self.createAction("Close &Tab",
                self.fileCloseTab, QKeySequence.Close, "filequit",
                "Close the active tab")
        fileQuitAction = self.createAction("&Quit", self.close,
                "Ctrl+Q", "filequit", "Close the application")
        editCopyAction = self.createAction("&Copy", self.editCopy,
                QKeySequence.Copy, "editcopy",
                "Copy text to the clipboard")
        editCutAction = self.createAction("Cu&t", self.editCut,
                QKeySequence.Cut, "editcut",
                "Cut text to the clipboard")
        editPasteAction = self.createAction("&Paste", self.editPaste,
                QKeySequence.Paste, "editpaste",
                "Paste in the clipboard's text")

        QShortcut(QKeySequence.PreviousChild, self, self.prevTab)
        QShortcut(QKeySequence.NextChild, self, self.nextTab)

        fileMenu = self.menuBar().addMenu("&File")
        self.addActions(fileMenu, (fileNewAction, fileOpenAction,
                fileSaveAction, fileSaveAsAction, fileSaveAllAction,
                fileCloseTabAction, None, fileQuitAction))
        editMenu = self.menuBar().addMenu("&Edit")
        self.addActions(editMenu, (editCopyAction, editCutAction,
                                   editPasteAction))

        fileToolbar = self.addToolBar("File")
        fileToolbar.setObjectName("FileToolbar")
        self.addActions(fileToolbar, (fileNewAction, fileOpenAction,
                                      fileSaveAction))
        editToolbar = self.addToolBar("Edit")
        editToolbar.setObjectName("EditToolbar")
        self.addActions(editToolbar, (editCopyAction, editCutAction,
                                      editPasteAction))

        settings = QSettings()
        self.restoreGeometry(settings.value("MainWindow/Geometry",
                QByteArray()))
        self.restoreState(settings.value("MainWindow/State",
                QByteArray()))

        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.showMessage("Ready", 5000)

        self.setWindowTitle("Tabbed Text Editor")
        QTimer.singleShot(0, self.loadFiles)


    def createAction(self, text, slot=None, shortcut=None, icon=None,
                     tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/{}.png".format(icon)))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action


    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)


    def closeEvent(self, event):
        failures = []
        for i in range(self.tabWidget.count()):
            textEdit = self.tabWidget.widget(i)
            if textEdit.isModified():
                try:
                    textEdit.save()
                except IOError as e:
                    failures.append(e)
        if (failures and
            QMessageBox.warning(self, "Text Editor -- Save Error",
                    "Failed to save{}\nQuit anyway?".format(
                    "\n\t".join(failures)),
                    QMessageBox.Yes|QMessageBox.No) ==
                    QMessageBox.No):
            event.ignore()
            return
        settings = QSettings()
        settings.setValue("MainWindow/Geometry", self.saveGeometry())
        settings.setValue("MainWindow/State", self.saveState())
        files = []
        for i in range(self.tabWidget.count()):
            textEdit = self.tabWidget.widget(i)
            if not textEdit.filename.startswith("Unnamed"):
                files.append(textEdit.filename)
        settings.setValue("CurrentFiles", files)
        while self.tabWidget.count():
            textEdit = self.tabWidget.widget(0)
            textEdit.close()
            self.tabWidget.removeTab(0)


    def prevTab(self):
        last = self.tabWidget.count()
        current = self.tabWidget.currentIndex()
        if last:
            last -= 1
            current = last if current == 0 else current - 1
            self.tabWidget.setCurrentIndex(current)


    def nextTab(self):
        last = self.tabWidget.count()
        current = self.tabWidget.currentIndex()
        if last:
            last -= 1
            current = 0 if current == last else current + 1
            self.tabWidget.setCurrentIndex(current)


    def loadFiles(self):
        if len(sys.argv) > 1:
            count = 0
            for filename in sys.argv[1:]:
                if QFileInfo(filename).isFile():
                    self.loadFile(filename)
                    QApplication.processEvents()
                    count += 1
                    if count >= 10: # Load at most 10 files
                        break
        else:
            settings = QSettings()
            files = settings.value("CurrentFiles") or []
            for filename in files:
                if QFile.exists(filename):
                    self.loadFile(filename)
                    QApplication.processEvents()


    def fileNew(self):
        textEdit = textedit.TextEdit()
        self.tabWidget.addTab(textEdit, textEdit.windowTitle())
        self.tabWidget.setCurrentWidget(textEdit)


    def fileOpen(self):
        filename = QFileDialog.getOpenFileName(self,
                "Tabbed Text Editor -- Open File")
        if filename:
            for i in range(self.tabWidget.count()):
                textEdit = self.tabWidget.widget(i)
                if textEdit.filename == filename:
                    self.tabWidget.setCurrentWidget(textEdit)
                    break
            else:
                self.loadFile(filename)


    def loadFile(self, filename):
        textEdit = textedit.TextEdit(filename)
        try:
            textEdit.load()
        except EnvironmentError as e:
            QMessageBox.warning(self,
                    "Tabbed Text Editor -- Load Error",
                    "Failed to load {}: {}".format(filename, e))
            textEdit.close()
            del textEdit
        else:
            self.tabWidget.addTab(textEdit, textEdit.windowTitle())
            self.tabWidget.setCurrentWidget(textEdit)


    def fileSave(self):
        textEdit = self.tabWidget.currentWidget()
        if textEdit is None or not isinstance(textEdit, QTextEdit):
            return True
        try:
            textEdit.save()
            self.tabWidget.setTabText(self.tabWidget.currentIndex(),
                    QFileInfo(textEdit.filename).fileName())
            return True
        except EnvironmentError as e:
            QMessageBox.warning(self,
                    "Tabbed Text Editor -- Save Error",
                    "Failed to save {}: {}".format(textEdit.filename, e))
            return False


    def fileSaveAs(self):
        textEdit = self.tabWidget.currentWidget()
        if textEdit is None or not isinstance(textEdit, QTextEdit):
            return True
        filename = QFileDialog.getSaveFileName(self,
                "Tabbed Text Editor -- Save File As", textEdit.filename,
                "Text files (*.txt *.*)")
        if filename:
            textEdit.filename = filename
            return self.fileSave()
        return True


    def fileSaveAll(self):
        errors = []
        for i in range(self.tabWidget.count()):
            textEdit = self.tabWidget.widget(i)
            if textEdit.isModified():
                try:
                    textEdit.save()
                except EnvironmentError as e:
                    errors.append("{}: {}".format(textEdit.filename, e))
        if errors:
            QMessageBox.warning(self, "Tabbed Text Editor -- "
                    "Save All Error",
                    "Failed to save\n{}".format("\n".join(errors)))


    def fileCloseTab(self):
        textEdit = self.tabWidget.currentWidget()
        if textEdit is None or not isinstance(textEdit, QTextEdit):
            return
        textEdit.close()


    def editCopy(self):
        textEdit = self.tabWidget.currentWidget()
        if textEdit is None or not isinstance(textEdit, QTextEdit):
            return
        cursor = textEdit.textCursor()
        text = cursor.selectedText()
        if text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text)


    def editCut(self):
        textEdit = self.tabWidget.currentWidget()
        if textEdit is None or not isinstance(textEdit, QTextEdit):
            return
        cursor = textEdit.textCursor()
        text = cursor.selectedText()
        if text:
            cursor.removeSelectedText()
            clipboard = QApplication.clipboard()
            clipboard.setText(text)


    def editPaste(self):
        textEdit = self.tabWidget.currentWidget()
        if textEdit is None or not isinstance(textEdit, QTextEdit):
            return
        clipboard = QApplication.clipboard()
        textEdit.insertPlainText(clipboard.text())


app = QApplication(sys.argv)
app.setWindowIcon(QIcon(":/icon.png"))
app.setOrganizationName("Qtrac Ltd.")
app.setOrganizationDomain("qtrac.eu")
app.setApplicationName("Tabbed Text Editor")
form = MainWindow()
form.show()
app.exec_()

