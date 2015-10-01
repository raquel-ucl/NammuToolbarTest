from .NammuView import NammuView
from ToolbarController import ToolbarController

class NammuController(object):

    def __init__(self):

        self.toolbarController = ToolbarController(self)
        self.view = NammuView(self)
        self.view.addToolBar(self.toolbarController.view)
        self.view.display()


    def onNewFileClick(self, event):
        """
        1. Check if current file in text area has unsaved changes
            1.1 Prompt user for file saving
                1.1.1 Save file
        2. Clear text area
        3. See GitHub issue: https://github.com/UCL-RITS/nammu/issues/6
        """
        print("NammuController: Creating new file...")

    def __getattr__(self, name):
        print "Undefined: "  + name
