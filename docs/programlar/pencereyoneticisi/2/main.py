# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import random

class duyuruPenceresi(Screen):
    pass

class atasozuPenceresi(Screen):
    pass

class resimPenceresi(Screen):
    pass

atasozleri=[
  'Abanın kadri yağmurda bilinir.',
  'Acı patlıcanı kırağı çalmaz.',
  'Aç bırakma hırsız edersin, çok söyleme arsız (yüzsüz) edersin.',
  'Misafir on kısmetle gelir; birini yer dokuzunu bırakır.'
]

resimler=[
  ('kiraz.jpg', 'İlçemizde bu yıl kiraz verimin yüksek olacağı beklenmektedir'),
  ('seftali.jpg', 'İlçemizde yetişen Şeftali\'ler tüm dünyaya satılıyor'),
  ('cilek.jpg', 'Çilek mevsimi geldi. Bol vitamin için çilek yiyin')
]

class IlanPanosuUyg(App):

    def build(self):
        self.py=ScreenManager()

        Builder.load_file("duyuru.kv")
        Builder.load_file("atasozu.kv")
        Builder.load_file("resim.kv")
        self.py.add_widget(duyuruPenceresi(name='ilan'))
        self.py.add_widget(atasozuPenceresi(name='atasozu'))
        self.py.add_widget(resimPenceresi(name='resim'))
        
        Clock.schedule_interval(self.pencereDegistir, 2)
        
        return self.py


    def pencereDegistir(self, *args):
        sonraki = self.py.next()
        pcr = self.py.get_screen(sonraki)
        if sonraki == 'duyuru':
            pcr.ids['duyuru_etiketi'].text = ' *Önümüzdeki hafta sonu veli toplantısı yapılacaktır.\n *Yarın gezi kolu Pamukkale\'ye gidecektir.'
        elif sonraki == 'atasozu':
             pcr.ids['atasozu_etiketi'].text = random.choice(atasozleri)
        elif sonraki == 'resim':
            res = random.choice(resimler)
            pcr.ids['resim'].source = res[0]
            pcr.ids['resim_etiketi'].text = res[1]
            
        self.py.current = sonraki






IlanPanosuUyg().run()
