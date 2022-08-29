'''
    KivyMS example program
    https://medium.com/@jdgb.projects/how-to-create-beautiful-apps-with-python-cecff9afebca
'''
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
    ''' MainApp '''
    def build(self):
        ''' build function '''
        return MDLabel(text="Hello, World", halign="center")


MainApp().run()
