from kivy.app import App
from kivy.core.window import Window
from os import listdir

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView



class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        print('ititialisation MainLayout')


class MyButton(Button):
    pass


class MyScreen(Screen):
    pass

class Note(BoxLayout):
    pass


class ProgramApp(App):
    def build(self):
        self.mainlayout = MainLayout()
        return self.mainlayout

    def update_notes(self) -> list:
        files = [*map(self.uncoding_notes, listdir('./notes'))]

        return

    def uncoding_notes(self, name_dir):
        pass


if __name__ == '__main__':
    ProgramApp().run()
