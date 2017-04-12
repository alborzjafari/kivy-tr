.. _pencereyoneticisi:

################################################################################################
:index:`Pencere Yöneticisi` (:index:`ScreenManager`)
################################################################################################

Kivy'de sekmeler, diğer GUI'lerde alışık olmadığımız pencere yöneticisi bulunmaktadır. Belki de :index:`yığın` lara (:index:`stacked widget`)
benzetebiliriz, ancak tam olarak eşleniği sayılamaz. Pencere yöneticisi tıpkı bir sunumdaki salyatlara da benzetleblir. Birden çok pencere 
düzennin arka arakya, yada istenilen herhangi bir sırada ekrana yansılıması olarak tanımlayabiliriz. Bazı Kivy programcıları atlı karınca 
iel pencere yönetcisi arasında seçim zorluğu da yaşamaktadırlar. Ancak pencere yönetici, bence diğer GUI'lerde de olması gereken muhteşem
bir yaıpıdır. Pencere yöneticisi sayesinde, Kivy ile kiosk tipi uygulalamaların geşiştirilmesi mümkün olabilmektedir.

Kod ile Pencere Yöneticisi
===========================

Pencere yöneticisini, kod ile hazırlayıp, her pencerenin içeriğini kv dili ile yazarız. Ancak nasıl çalıştığını anlamak için
öncelikle bir pencere yöneticisi olduşturalım ve bu pencereye sadece birer etiketden oluşan pecnereler ekleyelim. Pencere
yöneticisi ``ScreenManager`` parçacığı ile oluşturulur. Bu parçacığa eklenecek olan pencereler ise ``Screen`` parçacıklarıdır.
Bu açıklamalrdan sonra :numref:`Liste %s <py1>`'deki gibi bir program yazalım.


.. literalinclude:: ./programlar/pencereyoneticisi/1/main.py
    :linenos:
    :caption: main.py
    :name: py1
    :tab-width: 4
    :language: python

Bu programı açıklamaya çalışalım. Eğer pencere yöneticisi kullanacaksanız, ``build()`` işlevi mutlaka ``Screenmanager()`` parçacığı döndürmelidir.
Pencere yöneticisine ekleyeceğimiz her parçacık :index:`Screen()` olmalıdır. ``Screen()`` parçacığı, ekranda bağımsız bir pencere olarak görünecektir. 
Her pencereye mutalak bir isim vermelisiniz. Bunu ``name`` parametresi ile yapıyoruz. Daha sonra istediğiniz pencreye ait elemanlara erişmek veye bu pencereyi
ekrenda görüntülemek için bu ismi kullancakağız. Yukarıdaki programda pencereler, ``for`` iterasyonunun altında yapıldığında pencerelerin isimleri
sıra ile ``pncr0``, ``pncr1``, ``pncr2`` ve ``pncr3`` olmak üzere dört adet pencere eklenmiştir. 
Her pencereye yukarıda yaptığımız gibi tek bir parçacık ekleyecekseniz, bunu doğrudan ``add_widget()`` ile yapabilirsiniz. Birden fazla parçacık
barındıracak ise bunları herhengi bir pencere düzenine (Layout) ekleyip daha sonra bu pencere düzenin, pencreye eklemelisiniz. Yukarıdaki
programda pencereler arasında geçiş yapabilmek için zamanyalyıcı kullandık. Bunu daha önce açıklamıştık. Zamanlayıcının her tık deyişinde 
işletilen ``pencereDegistir()`` işlevinde her seferinde sonraki pencereye geçiş yapılmaktadır. Gösterilen pencereden sonraki pencerenin ismini, yöneticinin
``next()`` işlevi ile alabilirsiniz. ``pencereDegistir()`` işlevinde gösterilen penceredn sonraki pencere adı ``sonraki`` değişkenine aktarılmış, sonraki
satırda ise, gösterilecek pencere yöneticinin :index:`current` özelliğine atanmıştır. ``current`` hem atama yapılan hemde değeri çağrılan bir işlevdir, o
anda gösterilen pencerenin ismini barındırır.

Pencerelerin Kv Dili ile Hazırlanması
======================================
Her pencereyi ayrı ayrı kv dili ile hazırlayıp bunları pencere yöneticisine ekleyebiliriz. Öncelikle aşağıdaki üç pencereyi hazırlayalım:

.. literalinclude:: ./programlar/pencereyoneticisi/2/duyuru.kv
    :linenos:
    :tab-width: 4
    :caption: duyuru.kv
    :name: duyurupenceresi1

.. literalinclude:: ./programlar/pencereyoneticisi/2/atasozu.kv
    :linenos:
    :tab-width: 4
    :caption: atasozu.kv
    :name: atasozupenceresi1

.. literalinclude:: ./programlar/pencereyoneticisi/2/resim.kv
    :linenos:
    :tab-width: 4
    :caption: resim.kv
    :name: resimpenceresi1

Bu dosyalarda, şimdiye kadar farklı olarak yazdığımız sadece ``name`` belirteçleridir. Diğerlerini daha önceden biliyoruz.

programımız:

.. literalinclude:: ./programlar/pencereyoneticisi/2/main.py
    :linenos:
    :caption: main.py
    :name: py2
    :tab-width: 4
    :language: python

Burada, 
