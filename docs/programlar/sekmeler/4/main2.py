# -*- coding: utf-8 -*-

from kivy.app import App

from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class agacGorunumu(App):

    def build(self):
        duzen=BoxLayout(orientation='vertical')
        
        self.agac_koku = TreeView(hide_root=True, size_hint_y=0.8)
        
        kuruyemisler=[('Sert Kabuklular',('Ceviz', 'Fındık', 'Badem')), 
                      ('Meyve Kuruları',('Dut', 'Vişne', 'Kayısı', 'İncir'))]
        
        for ky in kuruyemisler:
            eb=self.agac_koku.add_node(TreeViewLabel(text=ky[0]))
            for k in ky[1]:
                self.agac_koku.add_node(TreeViewLabel(text=k),eb)

        duzen.add_widget(self.agac_koku)
        dgm=Button(text='Elemanları Yaz', size_hint_y=0.2)
        dgm.bind(on_press=self.elemanlari_yaz)
        duzen.add_widget(dgm)
        
        return duzen
        
        
    def elemanlari_yaz(self, *args):
        for eb in self.agac_koku.iterate_all_nodes():
            print eb.level, eb.text
            
        if self.agac_koku.selected_node:
            print "Seçili Eleman", self.agac_koku.selected_node.text
            
         
        print self.agac_koku.get_node_at_pos((1,1))
            
        #print dir(self.agac_koku)
agacGorunumu().run()
