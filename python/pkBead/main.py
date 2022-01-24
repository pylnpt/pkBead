from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from hover import HoverIconList

Window.maximize()


class Dashboard(Screen):
    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)
        self.update_tables()

    def update_tables(self):
        dt = MDDataTable(size_hint=(1, 1),
                         elevation=-1,
                         column_data=[
                             ("Product", dp(30)),
                             ("Order ID", dp(30)),
                             ("Purchased On", dp(30)),
                             ("Amount", dp(30)),
                             ("Tracking", dp(30)),
                             ("Status", dp(30)),
                         ],
                         row_data=[
                             (
                                 "Buffout",
                                 "#325689526",
                                 "12nd Dec 2021",
                                 "30 box",
                                 "GDKJSBC45",
                                 ("alert", [255 / 256, 165 / 256, 0, 1], "Pending")
                             ),
                             (
                                 "Super-Stimpack",
                                 "#325689526",
                                 "1st Jan 2021",
                                 "20 box",
                                 "GDKJSBC45",
                                 ("alert", [255 / 256, 165 / 256, 0, 1], "Pending")
                             ),
                             (
                                 "Mentat",
                                 "#325689526",
                                 "1st Dec 2021",
                                 "10 box",
                                 "GDKJSBC45",
                                 ("alert", [255 / 256, 165 / 256, 0, 1], "Pending")
                             ),
                             (
                                 "Jet",
                                 "#325689526",
                                 "8th Dec 2020",
                                 "40 box",
                                 "GDKJSBC45",
                                 ("checkbox-marked-circle", [0, 1, 0, 1], "Delivered")
                             ),
                             (
                                 "Psycho",
                                 "#325689526",
                                 "2nd Dec 2020",
                                 "10 box",
                                 "GDKJSBC45",
                                 ("alert-circle", [1, 0, 0, 1], "Canceled")
                             )
                         ])
        self.ids.display.add_widget(dt)


class Products(Screen):
    Builder.load_file("screens/products.kv")


class MainApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Dashboard(name="screen_one"))
        screen_manager.add_widget(Products(name="screen_two"))
        return screen_manager


if __name__ == "__main__":
    MainApp().run()



