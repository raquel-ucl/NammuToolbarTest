
from java.awt import BorderLayout
from javax.swing import JFrame
from __builtin__ import None

class NammuView(JFrame):

    def __init__(self, controller):

        #Give reference to controller to delegate action response
        self.controller = controller

        #All window components apart from the menu will go in the JFrame's
        #content pane
        self.setLayout(BorderLayout())

    def addToolBar(self, toolbarView):
        self.getContentPane().add(toolbarView, BorderLayout.NORTH)

    def display(self):

        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setTitle("~ Nammu v0.0.1 ~")
        self.pack()
        self.setLocationRelativeTo(None)

        #Display Nammu window
        self.visible = True
