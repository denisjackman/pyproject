'''
    https://avionmission.github.io/blog/kivymd-tutorial-01/
'''
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

class HomePage(MDScreen):  # pylint: disable=too-many-ancestors
    ''' home page '''


class MainApp(MDApp):
    '''
        main app object
    '''
    def build(self):
        ''' build '''
        Window.size = [300, 600]
        Builder.load_file('home_page.kv')
        return HomePage()

MainApp().run()
