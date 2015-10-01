import collections
from javax.swing import JToolBar, ImageIcon, JButton
from java.lang import ClassLoader


class ToolbarView(JToolBar):

    def __init__(self, controller):

        #Give reference to controller to delegate action response
        self.controller = controller

        options= ['NewFile', 'OpenFile', 'SaveFile', 'CloseFile', 'PrintFile', 'Undo', 'Redo',
                  'Copy', 'Cut', 'Paste', 'Validate', 'Lemmatise', 'Unicode',
                  'Console', 'Model', 'Settings', 'Help', 'About', 'Quit']
        methods = {}
        methods = collections.OrderedDict()
        for option in options:
            methods[option] = "on" + option + "Click"
            print methods[option]

        tooltips = {'NewFile': 'Creates empty ATF file for edition',
                 'OpenFile': 'Opens ATF file for edition',
                 'SaveFile': 'Saves current file',
                 'CloseFile': 'Closes current file',
                 'PrintFile': 'Prints current file',
                 'Undo': 'Undo last action',
                 'Redo': 'Redo last undone action',
                 'Copy': 'Copy text selection',
                 'Cut': 'Cut text selection',
                 'Paste': 'Paste clipboard content',
                 'Validate': 'Check current ATF correctness',
                 'Lemmatise': 'Obtain lemmas for current ATF text',
                 'Unicode': 'Use Unicode characters',
                 'Console': 'View/Hide Console',
                 'Model': 'Change to ATF data model view',
                 'Settings': 'Change Nammu settings',
                 'Help': 'Displays ATF documentation',
                 'About': 'Displays information about Nammu and ORACC',
                 'Quit': 'Exits Nammu'}

        for name, method in methods.items():
            icon = ImageIcon(self.findImageResource("NewFile"))
            button = JButton(icon, actionPerformed=getattr(self, "onNewFileClick"))
#            button = JButton(icon, actionPerformed=super(ToolbarView, self).__getattribute__("onNewFileClick"))
            button.setToolTipText(tooltips[name])
            self.add(button)
            #Work out is separator is needed
            if name in ['PrintFile', 'Redo', 'Paste', 'Lemmatise', 'Unicode',
                        'Console', 'Model', 'About']:
                self.addSeparator()

    def __getattr__(self, name):
        print "ToolbarView's getattr"
        return getattr(self.controller, name)

    #def onNewFileClick(self, event):
    #    self.controller.newFile()


    def findImageResource(self, name):
        #Create helper object to load icon images in jar
        loader = ClassLoader.getSystemClassLoader()
        #Load image
        return loader.getResource("resources/images/" + name.lower() + ".png")
