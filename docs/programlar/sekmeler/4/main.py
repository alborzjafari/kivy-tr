# -*- coding: utf-8 -*-

from kivy.app import App

from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class agacGorunumu(App):

    def build(self):
        duzen=BoxLayout(orientation='vertical')
        
        self.agac_koku = TreeView(hide_root=True)
        
        kuruyemisler=[('Sert Kabuklular',('Ceviz', 'Fındık', 'Badem')), 
                      ('Meyve Kuruları',('Dut', 'Vişne', 'Kayısı', 'İncir'))]
        
        for ky in kuruyemisler:
            eb=self.agac_koku.add_node(TreeViewLabel(text=ky[0]))
            for k in ky[1]:
                self.agac_koku.add_node(TreeViewLabel(text=k),eb)
        
        duzen.add_widget(self.agac_koku)
        
        return duzen
        
        
agacGorunumu().run()
