# -*- coding: utf-8 -*-

import os
import gettext
import sqlite3
import sqlite3 as lite
import sys

from functools import partial
#Icons are downloaded from http://icons.iconarchive.com, see licanses for individual icon.

TYPES=("INTEGER", "TEXT", "BOOLEAN", "NUMERIC", "BLOB")

gettext.bindtextdomain('kivysqlite', 'language')
 
 
from  kivy.lang import Builder

from kivy.app import App

from kivy.uix.popup import Popup 
from kivy.uix.treeview import TreeViewLabel
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox

def _(*args):
    return App.get_running_app().get_text(*args)
 
 
class fileOpenForm(Popup):
    pass 
 
 
class tableField(Popup):
    def __init__(self,**kwargs):
        self.myparent=kwargs['myparent']
        super(tableField,self).__init__(**kwargs)
        self.fi=-1
        if kwargs.has_key('fi'):
            self.fi=kwargs['fi']
        self.dropdown = DropDown()
        self.ids.field_pk.disabled=False
        self.ids.field_ai.disabled=False
        for typ in TYPES:
            btn = Button(text=typ, size_hint_y=None, height=25)
            self.dropdown.add_widget(btn)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            
 
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.ids.field_type, 'text', x))
        
        for f in self.myparent.fields:
            
            if f[4]:

                self.ids.field_pk.disabled=True
                self.ids.field_ai.disabled=True
                break

        if self.fi > -1:
            
            self.ids.field_name.text=self.myparent.fields[self.fi][0]
            self.ids.field_type.text=self.myparent.fields[self.fi][1]
            
            self.ids.field_not.active=self.myparent.fields[self.fi][2]
            self.ids.field_pk.active=self.myparent.fields[self.fi][3]
            self.ids.field_ai.active=self.myparent.fields[self.fi][4]
            
            if self.ids.field_ai.active:
                self.ids.field_pk.disabled=False
                self.ids.field_ai.disabled=False
            


    
       
    def add_field(self):
        field_name=self.ids.field_name.text
        field_type=self.ids.field_type.text
        
        field_not=self.ids.field_not.active
        field_pk=self.ids.field_pk.active
        field_ai=self.ids.field_ai.active

        if field_ai: field_pk=True
        
        f_exist=False
        
        if self.fi == -1:
            for f in self.myparent.fields:
                if f[0]==field_name:
                    f_exist=True
                    break
                
        
        if field_type==_('Select Type') or not field_name:
            popup = Popup(title=_('Warning !'), content=Label(text=_("You should write field name and select type")), size_hint = (0.5,0.4) )
            popup.open()
        
        elif f_exist:
            popup = Popup(title=_('Warning !'), content=Label(text=_("This field name already exists")), size_hint = (0.5,0.4) )
            popup.open()
            
        else:
            ft=(field_name, field_type, field_not, field_pk, field_ai)
            if self.fi == -1:
                self.myparent.fields.append(ft)
            else:
                self.myparent.fields[self.fi]=ft
            self.dismiss()
            
            

            
            self.myparent.update_list()
 
 
class newTableForm(Popup):
    def __init__(self,**kwargs):
        #self.parent=kwargs['parent']
        super(newTableForm,self).__init__(**kwargs)
        self.fields=[]
        self.update_list()
        
        
        
    
    def add_field(self):
    
        form=tableField(title=_("Add Field"), size_hint=(.6, .6), myparent=self)
        form.open()
        
        
    def get_selected_index(self):
        rm_index=-1
        c=0
        rmn=-1
        for f in self.ids.table_fields.children:
            if type(f)==type(CheckBox()):
                if f.active:
                    rm_index=c
                    break
                c +=1
        
        if rm_index > -1:
            rmn=len(self.fields)-rm_index-1
        
        return rmn
            
    def remove_field(self):
            rmn=self.get_selected_index()
            if rmn > -1:
                self.fields.pop(rmn)
                self.update_list()
        
        
    def edit_field(self):
        fi=self.get_selected_index()
        if fi > -1:
            form=tableField(title=_("Edit Table Field"), size_hint=(.6, .6), myparent=self, fi=fi)
            form.open()

        
        
    def update_list(self):
        chlist=[]
        for c in self.ids.table_fields.children:
            chlist.append(c)
            
        for cx in chlist[:]:
            self.ids.table_fields.remove_widget(cx)
       
        for header in (_("Selection"), _("Name"), _("Type"), _("Not"), _("PK"), _("AI")):
            self.ids.table_fields.add_widget(Label(text=header, size_hint_y=0.1))
       
        for f in self.fields:
            rb=CheckBox()
            rb.group='selection'
            self.ids.table_fields.add_widget(rb)
            self.ids.table_fields.add_widget(Label(text=f[0]))
            self.ids.table_fields.add_widget(Label(text= f[1]))
            self.ids.table_fields.add_widget(Label(text= '√' if f[2] else ''))
            self.ids.table_fields.add_widget(Label(text= '√' if f[3] else ''))
            self.ids.table_fields.add_widget(Label(text= '√' if f[4] else ''))

            
 
 
 

class ConfirmPopup(Popup):
    def __init__(self,**kwargs):
        self.text= kwargs['text']
        self.register_event_type('on_answer')
        super(ConfirmPopup,self).__init__(**kwargs)
        self.text= kwargs['text']
        self.result=None
    
    def on_answer(self, *args):
        pass
    
 
 
class KivySQLiteApp(App):

    def build(self):
        self.recent_path=os.getcwd()
        self.cursor=None
        self.set_language('tr')
        self.conn=None
        return Builder.load_file('main.kv')
          
          
          
    def newTableForm(self):
        popup=newTableForm(title=_("Create New Table"))
        popup.open()
          
          
    def showError(self, text):
        content=Label(text=text, markup=True)
        popup = Popup(title=_('Warning !'), content=content)
        popup.size_hint = (0.7,0.7)

        popup.open()

          
    def fileOpenDialog(self):
        form = fileOpenForm()
        form.open()


    def openDB(self, db_select):

        try: 
            self.conn = lite.connect(db_select.selection[0])
        except:
            self.showError(_("Error open db"))
            return

        self.cursor = self.conn.cursor()
        self.update_tables_tree()
        self.root.ids.new_table_action.disabled=False
        self.root.ids.delete_table_action.disabled=False
       

        
    def update_tables_tree(self):
    
        for node in self.root.ids.table_tree.iterate_all_nodes():
    
            self.root.ids.table_tree.remove_node(node)
    
        if self.conn:
            for typ in ('table','view'):
                self.cursor.execute("SELECT name FROM sqlite_master WHERE type = '%s'" % typ)
                result=self.cursor.fetchall()
                if result:
                    tvlabeltext='{0} ({1})'.format( _(typ.title()+'s'), len(result) )
                    tvlabel=TreeViewLabel(text=tvlabeltext)
                    parent_node=self.root.ids.table_tree.add_node(tvlabel)
                    for tb in result:
                        tvlabel=TreeViewLabel(text=tb[0], markup=True)
                        tvlabel.tbtype=typ
                        tvlabel.tbname=tb[0]
                        tb_node=self.root.ids.table_tree.add_node(tvlabel, parent_node)
                        
                        self.cursor.execute('PRAGMA TABLE_INFO(`%s`)' % tb[0])
                        
                        for field in self.cursor.fetchall():
                            tvlabeltext='[b]{0}[/b]    {1}'.format( field[1], field[2] )
                            tvlabel=TreeViewLabel(text=tvlabeltext, markup=True)               
                            self.root.ids.table_tree.add_node(tvlabel, tb_node)

                    
            
        
    def deleteTableDialog(self):
        tb=self.root.ids.table_tree.selected_node
        if hasattr(tb,'tbtype'):
            form = ConfirmPopup(text=_("All data in the table you selected will be deleted!\n Are you sure you want to delete table [b]%s[/b]?") % tb.text)

            form.bind(on_answer=self.delete_table)
            form.open()
        
        
    def closeDB(self):
        if self.conn:
            self.conn.close()
            self.conn=None
            self.update_tables_tree()
            self.root.ids.delete_table_action.disabled=True
            
        
    def tree_view_expanded(self):
        pass
        
    def delete_table(self, instance, answer):
        tb=self.root.ids.table_tree.selected_node
        
        if hasattr(tb,'tbtype'):
            if answer=='yes':
                try:
                    self.cursor.execute('DROP TABLE `%s`' % tb.tbname)
                except Exception as error:
                    self.showError(_("An error occurred while droping table.\nThe message returned by sqlite engine is:")+"\n"+str(error))
                
                self.update_tables_tree()
        
        instance.dismiss()
      
    def set_language(self,selectedLanguage):
        self.t = gettext.translation('kivysqlite', 'language', languages=[selectedLanguage], fallback=True)

 
    def get_text(self, *args):
        return self.t.ugettext(*args)
    

 
if __name__ == '__main__':
    KivySQLiteApp().run()
