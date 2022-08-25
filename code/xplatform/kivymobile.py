'''
# Develop Mobile Apps with Kivy
# pip install kivy
'''
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.checkbox import CheckBox    
from kivy.uix.image import Image
from kivy.uix.popup import Popup

class MobileApp(App):
    ''' mobile app '''
    def build(self):
        '''
            build function
        '''
        # Layout of App
        layout = BoxLayout(orientation="vertical")# Label 
        label = Label(text="Hello Kivy!")# Button
        btn = Button(text="Click Me!")# Button Action
        btn.bind(on_press=self.btn_pressed)# Input Box
        input_box = TextInput(hint_text="Input Here",size_hint=(.3,.2))# Check Box
        check_box = CheckBox(text="Check Me!")

        # ScrollView
        scroll_view = ScrollView()
        grid_layout = GridLayout(cols=2, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))
        # Add Image to App
        image = Image(source="medium.png")# Popup
        popup = Popup(title="Popup", size_hint=(.5,.5))

        # Add to layout
        layout.add_widget(label)
        layout.add_widget(btn)
        layout.add_widget(input_box)
        layout.add_widget(scroll_view)
        layout.add_widget(check_box)
        layout.add_widget(image)
        layout.add_widget(popup)
        return layout

    def btn_pressed(self, instance):
        ''' button pressed '''
        print("Button Pressed!")# Run the App

app = MobileApp()
app.run()