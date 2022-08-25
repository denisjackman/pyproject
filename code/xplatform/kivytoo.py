'''
    Kivy example 
        https://medium.com/@jdgb.projects/how-to-create-beautiful-apps-with-python-cecff9afebca
'''
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    ''' MD class object '''
    def build(self):
        ''' build '''
        return Builder.load_file("firstapp.kv")
    def change_label(self):
        ''' label change '''
        if self.root.ids.label.text == "Button pressed":
            self.root.ids.label.text="Press That Button"
        else:
            self.root.ids.label.text="Button pressed"

MainApp().run()
