import collections
from javax.swing import JToolBar, ImageIcon, JButton
from java.lang import ClassLoader


class ToolbarView(JToolBar):

    def __init__(self, controller):

        #Give reference to controller to delegate action response
        self.controller = controller

        tooltips = {}
        tooltips = collections.OrderedDict()
        tooltips['newFile'] = 'Creates empty ATF file for edition'
        tooltips['openFile'] = 'Opens ATF file for edition'
        tooltips['saveFile'] = 'Saves current file'
        tooltips['closeFile'] = 'Closes current file'

        for name, tooltip in tooltips.items():
            print name, tooltip
            icon = ImageIcon(self.findImageResource(name))
            button = JButton(icon, actionPerformed = getattr(self, name))
            button.setToolTipText(tooltips[name])
            self.add(button)
            #Work out is separator is needed
            if name in ['openFile', 'redo']:
                self.addSeparator()


    def __getattr__(self, name):
        print "ToolbarView's getattr"
        return getattr(self.controller, name)

    def findImageResource(self, name):
        #Create helper object to load icon images in jar
        loader = ClassLoader.getSystemClassLoader()
        #Load image
        return loader.getResource("resources/images/" + name + ".png")
