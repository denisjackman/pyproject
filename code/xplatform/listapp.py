'''
    note app 
    https://medium.com/@jdgb.projects/the-first-best-app-you-can-create-with-kivy-6a3efcf3d12c
    updated to make sure it works 
'''
from kivy.lang import Builder
from kivymd.app import MDApp
#from kivy.uix.widget import Widget
#from kivymd.uix.label import MDLabel
#from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import OneLineIconListItem,IconLeftWidget
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivymd.uix.screen import MDScreen

class ListScreen(Screen):
    '''
        list screen object
    '''
    pass

class TextScreen(Screen):
    '''
        text screen object
    '''
    pass

class MainApp(MDApp):
    '''
        mainapp object
    '''
    def build(self):
        '''
            build object
        '''
        self.sm=ScreenManager()
        self.sm.add_widget(ListScreen(name="list"))
        self.sm.add_widget(TextScreen(name="text"))
        return self.sm

    def add_note(self):
        '''
            add note function 
        '''
        note=self.root.get_screen('list').ids.note.text
        new=OneLineIconListItem(text=note)
        icon=IconLeftWidget(icon="trash-can")
        new.add_widget(icon)
        self.root.get_screen('list').ids.container.add_widget(new)
        new.bind(on_release=self.ReadNote)
        icon.bind(on_release=self.delete)

    def delete(self,Widget):
        '''
            delete a note function 
        '''
        self.root.get_screen('list').ids.container.remove_widget(Widget.parent.parent)

    def ReadNote(self,Widget):
        '''
            read note function
        '''
        self.sm.current = "text"
        text=Widget.text
        self.root.get_screen('text').ids.fulldescription.text=text

MainApp().run()