from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder


class ABCBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create three buttons
        button_a = Button(text="A")
        button_b = Button(text="B")
        button_c = Button(text="C")

        # Add the buttons to the layout
        self.add_widget(button_a)
        self.add_widget(button_b)
        self.add_widget(button_c)

        # Bind the on_press event of each button to the callback function
        button_a.bind(on_press=self.on_button_press)
        button_b.bind(on_press=self.on_button_press)
        button_c.bind(on_press=self.on_button_press)

    def on_button_press(self, button):
        print(f"Button {button.text} clicked!")


# Load the KV language file after defining the classes
Builder.load_file("TheLab.kv")

class TheLabApp(App):
    def build(self):
        return ABCBoxLayout()

TheLabApp().run()