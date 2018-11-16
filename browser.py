# -*- coding: utf-8 -*-
# Copyright: Arthur Milchior <arthur@milchior.fr>
# Based on anki code by Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in https://github.com/Arthur-Milchior/anki-relation
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from . import merge
from .utils import *
from anki.hooks import addHook
import aqt

def searchRelationsInBrowser(relations):
    browser = aqt.dialogs.open("Browser", mw)
    browser.form.searchEdit.lineEdit().setText(queryRelated(relations))
    browser.onSearchActivated()

def searchRelatedNotesInBrowser(browser):
    searchRelationsInBrowser(getRelationsFromNotes(getSelectedNotes(browser)))

def setupMenu(browser):
    for (shortcut, text, function) in [
            ("Ctrl+Shift+Alt+E","See related notes",searchRelatedNotesInBrowser),
            ("Ctrl+Alt+E","Create a relation",merge.createRelation),
            #(None,"Merge the selected relations",merge.mergeRelations),
    ]:
        a=QAction(text,browser)
        a.setShortcut(QKeySequence(shortcut))
        a.triggered.connect(lambda function=function: function(browser))
        browser.form.menuEdit.addAction(a)
        
        # a=QAction("Merge the selected relations/notes",browser)
        # a.triggered.connect(lambda: merge.mergeRelations(browser))
        # browser.form.menuEdit.addAction(a)
addHook("browser.setupMenus", setupMenu)

