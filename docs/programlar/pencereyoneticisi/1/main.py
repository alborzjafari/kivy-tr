# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

class PencereUyg(App):

    def build(self):
        self.py=ScreenManager()

        for i in range(4):
            p=Screen(name="pncr%d" % i)
            p.add_widget(Label(text="Pencere %d" % i))
            self.py.add_widget(p)
        self.py.current = 'pncr2'
        Clock.schedule_interval(self.pencereDegistir, 2)
        return self.py

    def pencereDegistir(self, *args):
        sonraki = self.py.next()
        self.py.current = sonraki

PencereUyg().run()
