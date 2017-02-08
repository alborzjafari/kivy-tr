# -*- coding: utf-8 -*-

from kivy.app import App

from kivy.uix.treeview import TreeView, TreeViewLabel

class agacGorunumu(App):

    def build(self):
        agac_koku = TreeView()
        ebeveyn1=agac_koku.add_node(TreeViewLabel(text='Ebeveyn 1'))
        
        cocuk11=agac_koku.add_node(TreeViewLabel(text='Çocuk 1 1'), ebeveyn1)
        cocuk12=agac_koku.add_node(TreeViewLabel(text='Çocuk 1 2'), ebeveyn1)
        
        cocuk121=agac_koku.add_node(TreeViewLabel(text='Çocuk 1 2 1'), cocuk12)
        cocuk122=agac_koku.add_node(TreeViewLabel(text='Çocuk 1 2 2'), cocuk12)
        
        ebeveyn2=agac_koku.add_node(TreeViewLabel(text='Ebeveyn 2'))
        cocuk21=agac_koku.add_node(TreeViewLabel(text='Çocuk 2 1'), ebeveyn2)
        cocuk22=agac_koku.add_node(TreeViewLabel(text='Çocuk 2 2'), ebeveyn2)

        
        return agac_koku
        
agacGorunumu().run()
