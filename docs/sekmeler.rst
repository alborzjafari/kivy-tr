.. _sekmeler:

################################################################################################
:index:`Sekmeli Panel` (:index:`TabbedPanel`) ve :index:`Ağaç Görünümü` (:index:`TreeView`)
################################################################################################

Kivy'de sekmeler, diğer GUI'lerde olduğu gibi bir pencerede birden fazla sayfa görünümünü sunmak için kullanılır. Kivy'de `Sekmeli Panel`
(`TabbedPanel`) olarak isimlendirilir. Oluşturulduğunda size ön tanımlı olarak ``Default`` sekmesini sunacaktır.

Kod ile Sekmeli Panel Oluşturulması
====================================

Her zaman olduğu gibi, öncelikle kod ile nasıl sekmeli panel oluşturacağımızı göreceğiz. Sözü fazla uzatmadan hemen örnek kodumuzu verelim, programımızı 
:numref:`Liste %s <sekme1>`'deki gibi yazalım.


.. literalinclude:: ./programlar/sekmeler/1/main.py
    :linenos:
    :caption: main.py
    :name: sekme1
    :tab-width: 4
    :language: python

Şimdi burada olup biteni anlamaya çalışalım. Bir sekmeli panel ``TabbedPanel()`` parçacığı ile oluşturulur. Bir sekmeli panle oluşur oluşmaz ön tanımlı 
olarak :index:`default panel` ile oluştur ve bu ön tanımlı sekme sekme parçacığının özelliklerine :index:`default_tab` ın  ``text`` ve ``content`` 
özelliklerini kullarak yapabilirsiniz. Aslında bunu :index:`default_tab_text` ve :index:`default_tab_content` ile de yapmanız mümkün ancak ben öncekini
tercih ediyorum. Bunlardan ilki sekme başlığını ikincisi sekmenin içeriğini belirtir. Programımızda ön tanımlı sekmenin başlığını
``İlk Sekme`` içeriğini ise bir etiketten oluşturduk (etiket metinini açıklamaya gerek yok sanırım). Eğer ön tanımlı sekmeyi istemiyorsanız, 
sekmeli paneli oluştururken :index:`do_default_tab` parametresinin değerini ``False`` yapmalısınız. Diğer bir deyişye, ön tanımlı sekmesi olmayan bir
sekmeli paneli şu şekilde tanımlayabilirdik:

::

    sekmeli_panel = TabbedPanel(do_default_tab=False)
    
Sekmeli Panele yeni sekmeler eklemek için, öncelikle bu sekmeyi hazırlamanız gerekir. Bunu sekme parçacığı :index:`TabbedPanelHeader()` kullanarak
yaparız. Bu parçacığın ``text`` özelliği sekmenin başlığını gösterir. İçeriğini ise, :index:`content` özelliği ile oluşturabilirsiniz. ``content``
özelliğine istediğiniz bir pencere düzeni atayabilirsiniz. Burada basit olsun diye sadece bir etiket atadık. 

Programımız önce ön tanımlı sekme oluşturuyor. Daha sonra bir sekme başlıkları "Sekme <sayi>" ve sekme içeriklerindeki etiketlerin metinleri
"Bu sekmenin sahibi: <isim>" olacak şekilde yeni sekme parçacıkları oluşturup bunları Sekmeli Panele ekliyor. Programımız çalıştığında 
:numref:`Şekil %s <sekmeler-sekme1Img>`'deki gibi olacaktır.


.. _sekmeler-sekme1Img:

.. figure:: ./programlar/sekmeler/1/sekme1.png

   Dört sekmeli panel
   
Şimdi biraz olaylara bakalım. İlk olarak ön tanımlı sekmeye geçiş yapıldığında oluşan olayı bir işeleve bağlayalım:

::

    sekmeli_panel.default_tab.bind(on_release = self.sekmeDegistirildi)
    
    
Bu satırı ``return`` den hemen önce yazabilirsiniz. ``sekmeDegistirildi()`` işlevini de şu şekilde yazalım:

::

    def sekmeDegistirildi(self,sekme):
        popup = Popup(title='Sekme Değiştirildi',
                      content=Label(text= "Sekme Başlığı: "+sekme.text),
                      size_hint=(None, None), size=(200, 200))
        popup.open()
    

Bu işlevi yazdıktan sonra programınızın başına aşağıdaki saırı yazarak ``Popup`` perçacaığını içermelisiniz:

::

    from kivy.uix.popup import Popup
   
   
Şimdi programınızı çalışrırın ve bir sekmeye geçtikten sonra tekrar ön tanımlı sekmeye geçiş yapın. Popup penceres açılacaktır. İsterseniz tüm sekmelere
geçiş yaptığınızda bu popup penceresini görüntülemek için ``for`` döngü bloğunu btirmeden önce aşağıdaki satırı ekleyebilirsiniz:

::

    sekme.bind(on_release = self.sekmeDegistirildi) 
   
kv Dili ile Sekmeli Panel Oluşturulması
========================================

Şimdi kv dili ile nasıl sekme oluşturabileceğimize bakalım. Sekmeli panleimizde hiçbir işlev yapmadan sadece oluşturalım. İlk olarak programımızı 
:numref:`Liste %s <sekme2>`'deki gibi yazalım.


.. literalinclude:: ./programlar/sekmeler/2/main.py
    :linenos:
    :caption: main.py
    :name: sekme2
    :tab-width: 4
    :language: python


kv dosyasını da :numref:`Liste %s <sekme_kv2>`'deki gibi yazalım.

.. literalinclude:: ./programlar/sekmeler/2/sekmelipanel.kv
    :linenos:
    :caption: sekmelipanel.kv
    :name: sekme_kv2
    :tab-width: 4

Burada gördüğünüz gibi ikinci sekemede bir etiket ve bir işlevsiz düğme bulunmaktadır. Son sekemde ise sadece bir resim bulunuyour.
``main.py`` programını çalıştıracak olursak, :numref:`Şekil %s <sekmeler-sekme2Img>`'deki gibi olacaktır.


.. _sekmeler-sekme2Img:

.. figure:: ./programlar/sekmeler/2/sekme2.png

   Dört sekmeli panel

Ağaç Görünümü (TreeView)
=========================

Aslında ağaç görünümüne daha önceden tanış olduk. Dosya açma diyaloğunda (:ref:`dosya_ac`) kullandığımız ``FileChooserListView`` modülünde
ağaç görünümü kullanılmaktadır. Bir ağaç görünümü şu şekildedir::

  Kök
   |
   +--Ebeveyn 1
   |   |
   |   +--Çocuk 1 1
   |   |
   |   +--Çocuk 1 2
   |     |
   |     +--Çocuk 1 2 1
   |     |
   |     +--Çocuk 1 2 2
   |   
   +--Ebeveyn 2
       |
       +--Çocuk 2 1
       |
       +--Çocuk 2 2         

Burada her ebeveynin kendi çocuğu vardır. Şimdi böyle bir yapıyı nasıl oluşturacağımıza bakalım. Önce program ile nasıl yapılacağına bakacağız. 
:numref:`Liste %s <agac1>`'deki programı inceleyin


.. literalinclude:: ./programlar/sekmeler/3/main.py
    :linenos:
    :caption: main.py
    :name: agac1
    :tab-width: 4
    :language: python

Bir ağaç kökü ``TreeView()`` nesnesi ile oluşturulur. Daha sonra ebeveynler ve çocuklar bu ağaç köküne :index:`add_node` ile eklenir. Eklenen her elemana 
:index:`düğüm` (:index:`node`) diyoruz. Tüm ebeveynler
ve çocuklar ağaç köküne eklenir, yani beklendiği gibi, çocuklar önceki ebeveynlerine değil, doğrudan ağaç köküne eklenir, ancak hangi ebeyene ekleneceği,
``add_node()`` işevinin ikinci argümanı olarak belirtilir. Eğer argüman berlirtilemz ise, doğrudan köke eklenir. Programımızı çalıştırdığımızda 
:numref:`Şekil %s <sekmeler-agac1Img>`'deki gibi bir görüntü elde ederiz.



.. _sekmeler-agac1Img:

.. figure:: ./programlar/sekmeler/3/agac1.png

   Ağaç görünümü

Elimizdeki veriseti ile bir ağaç kökünü :numref:`Liste %s <agac2>`'deki gibi doldurabiliriz:

.. literalinclude:: ./programlar/sekmeler/4/main.py
    :linenos:
    :caption: main.py
    :name: agac2
    :tab-width: 4
    :language: python

Bu programda ağaç kökünü :index:`hide_root` ile gizlediğimize dikkat ediniz.

Peki seçilen elemana ya da tüm elemanlara nasıl ulaşacağız? Düğümler üzerinde iterasyonu :index:`iterate_all_nodes()` ile yapabiliriz.
:numref:`Liste %s <agac2>`'deki programdaki 
elemanlara ulaşmak için önce düzenimize bir düğme ekleyelim. Aşağıdaki kodu ``return`` den hemen önce yazın::

    dgm=Button(text='Elemanları Yaz', size_hint_y=0.2)
    dgm.bind(on_press=self.elemanlari_yaz)
    duzen.add_widget(dgm)
    
Daha sonra düğmeye tıklandığında çağrılacak olan işlevi yazalım::

    def elemanlari_yaz(self, *args):
        for eb in self.agac_koku.iterate_all_nodes():
            print eb.level, eb.text
            
Düğmeye tıkladığımızda ekrana elemanların konumları ve elemanlar yazılacaktır.

Eğer seçili olan elemana ulaşmak istiyorsanız :index:`selected_node()` özelliğini kullanabilirsiniz. Aşağıdaki satırı ``elemanlari_yaz()``
işlevinin sonuna ekleyin ve düğmeye tıklayın::

    if self.agac_koku.selected_node:
        print "Seçili Eleman", self.agac_koku.selected_node.text
        
Eğer önceden bir düğümü açılı yapmak istiyorsanız :index:`select_node` özelliğini kullanabilirsiniz. Örneğin
