# -*- coding: utf-8 -*-
# Copyright: Arthur Milchior <arthur@milchior.fr>
# Based on anki code by Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in https://github.com/Arthur-Milchior/anki-relation
# Addon number 413416269  https://ankiweb.net/shared/info/413416269
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import aqt
from anki.hooks import addHook

from . import merge
from .utils import getRelationsFromNotes, getSelectedNotes, queryRelated


def searchRelationsInBrowser(relations):
    browser = aqt.dialogs.open("Browser", aqt.mw)
    browser.form.searchEdit.lineEdit().setText(queryRelated(relations))
    browser.onSearchActivated()


def searchRelatedNotesInBrowser(browser):
    searchRelationsInBrowser(getRelationsFromNotes(getSelectedNotes(browser)))


def setupMenu(browser):
    a = QAction("See related notes", browser)
    a.setShortcut(QKeySequence("Ctrl+Shift+Alt+E"))
    a.triggered.connect(lambda: searchRelatedNotesInBrowser(browser))
    browser.form.menuEdit.addAction(a)

    a = QAction("Create a relation", browser)
    a.setShortcut(QKeySequence("Ctrl+Alt+E"))
    a.triggered.connect(lambda: merge.createRelationBrowser(browser))
    browser.form.menuEdit.addAction(a)


addHook("browser.setupMenus", setupMenu)
