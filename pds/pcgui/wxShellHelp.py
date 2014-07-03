"""
This should be run as a child window from wxShell
"""
########################################################################

from PythonCard import model, dialog
import wx
import os
import types

from  pds.pcgui.wxUtil import wxUtil
from  pds.shell import HELP_STR, HELP_USE_STR

########################################################################

wxShellHelpTxt = """\n
************************* wxShell HELP **************************
This is the wxWindows graphical interface for PDS.  

*****************************************************************\n
"""

###########################################################
class wxShellHelp(model.Background, wxUtil):

    ###########################################################
    def on_initialize(self, event):
        # Initialization
        # including sizer setup, do it here
        # self.setupSizers()
        self.help = wxShellHelpTxt + HELP_STR + HELP_USE_STR
        self.components.HelpText.text = self.help

    ###########################################################
    def on_menuFileExit_select(self,event): 
        self.close()
