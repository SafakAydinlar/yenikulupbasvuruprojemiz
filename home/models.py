

from django.db import models


class Basvuru(models.Model):
    name = models.CharField(max_length=50,blank= True)  #blank = false, boş geçilememesini sağlar
    surname = models.CharField(max_length=30,blank= True)
    tckimlik = models.CharField(max_length=11 ,blank= True,unique=True) #eşsiz olmasını sağladım
    telefon = models.CharField(max_length=30 ,blank= True)
    tecrübe = models.CharField(max_length=50 ,blank= True)
    message = models.CharField(max_length=30,blank= True )
    #onay = models.BooleanField(verbose_name="Onay", default=False, blank=False)
    confirmed = models.BooleanField(verbose_name="Durum", default=False)

    posta = models.EmailField(blank=True) #boş geçilemez

    BOLUMLER =[

            ('SPO', 'Spor'),
            ('FEN', 'Fen Bilimleri'),
            ('MUH', 'Mühendislik'),
    ]
    bolum = models.CharField(max_length=3, choices=BOLUMLER,default=BOLUMLER[2][0])
    #seçimli modeller = bölümler - cinsiyet ----> Fen bilimleri veritabanında fen olarak tutulacak örneğin. 

    CİNSİYET_TABLOSU = [
        
        ('e','Erkek'), 
        ('h','Kadın'),
        ('b', 'Belirtmek istemiyorum'),
        ]
    
    cinsiyet=models.CharField(choices=CİNSİYET_TABLOSU, max_length=11, default=CİNSİYET_TABLOSU[2][0])

    class Meta:
        verbose_name_plural = 'CEC Başvuruları' 




class Basvuru2(models.Model):
    name = models.CharField(max_length=50,blank= True)  #blank = false, boş geçilememesini sağlar
    surname = models.CharField(max_length=30,blank= True)
    tckimlik = models.CharField(max_length=11 ,blank= True,unique=True) #eşsiz olmasını sağladım
    telefon = models.CharField(max_length=30 ,blank= True)
    tecrübe = models.CharField(max_length=50 ,blank= True)
    message = models.CharField(max_length=30,blank= True )
    #onay = models.BooleanField(verbose_name="Onay", default=False, blank=False)
    confirmed = models.BooleanField(verbose_name="Durum", default=False)

    posta = models.EmailField(blank=True) #boş geçilemez

    BOLUMLER =[

            ('SPO', 'Spor'),
            ('FEN', 'Fen Bilimleri'),
            ('MUH', 'Mühendislik'),
    ]
    bolum = models.CharField(max_length=3, choices=BOLUMLER,default=BOLUMLER[2][0])
    #seçimli modeller = bölümler - cinsiyet ----> Fen bilimleri veritabanında fen olarak tutulacak örneğin. 

    CİNSİYET_TABLOSU = [
        
        ('e','Erkek'), 
        ('h','Kadın'),
        ('b', 'Belirtmek istemiyorum'),
        ]
    
    cinsiyet=models.CharField(choices=CİNSİYET_TABLOSU, max_length=11, default=CİNSİYET_TABLOSU[2][0])

    class Meta:
        verbose_name_plural = 'SEC Başvuruları' 




    


class Basvuru3(models.Model):
    name = models.CharField(max_length=50,blank= True)  #blank = false, boş geçilememesini sağlar
    surname = models.CharField(max_length=30,blank= True)
    tckimlik = models.CharField(max_length=11 ,blank= True,unique=True) #eşsiz olmasını sağladım
    telefon = models.CharField(max_length=30 ,blank= True)
    tecrübe = models.CharField(max_length=50 ,blank= True)
    message = models.CharField(max_length=30,blank= True )
    #onay = models.BooleanField(verbose_name="Onay", default=False, blank=False)
    confirmed = models.BooleanField(verbose_name="Durum", default=False)

    posta = models.EmailField(blank=True) #boş geçilemez

    BOLUMLER =[

            ('SPO', 'Spor'),
            ('FEN', 'Fen Bilimleri'),
            ('MUH', 'Mühendislik'),
    ]
    bolum = models.CharField(max_length=3, choices=BOLUMLER,default=BOLUMLER[2][0])
    #seçimli modeller = bölümler - cinsiyet ----> Fen bilimleri veritabanında fen olarak tutulacak örneğin. 

    CİNSİYET_TABLOSU = [
        
        ('e','Erkek'), 
        ('h','Kadın'),
        ('b', 'Belirtmek istemiyorum'),
        ]
    
    cinsiyet=models.CharField(choices=CİNSİYET_TABLOSU, max_length=11, default=CİNSİYET_TABLOSU[2][0])

    class Meta:
        verbose_name_plural = 'AI Başvuruları' 




class Basvuru4(models.Model):
    name = models.CharField(max_length=50,blank= True)  #blank = false, boş geçilememesini sağlar
    surname = models.CharField(max_length=30,blank= True)
    tckimlik = models.CharField(max_length=11 ,blank= True,unique=True) #eşsiz olmasını sağladım
    telefon = models.CharField(max_length=30 ,blank= True)
    tecrübe = models.CharField(max_length=50 ,blank= True)
    message = models.CharField(max_length=30,blank= True )
    #onay = models.BooleanField(verbose_name="Onay", default=False, blank=False)
    confirmed = models.BooleanField(verbose_name="Durum", default=False)

    posta = models.EmailField(blank=True) #boş geçilemez

    BOLUMLER =[

            ('SPO', 'Spor'),
            ('FEN', 'Fen Bilimleri'),
            ('MUH', 'Mühendislik'),
    ]
    bolum = models.CharField(max_length=3, choices=BOLUMLER,default=BOLUMLER[2][0])
    #seçimli modeller = bölümler - cinsiyet ----> Fen bilimleri veritabanında fen olarak tutulacak örneğin. 

    CİNSİYET_TABLOSU = [
        
        ('e','Erkek'), 
        ('h','Kadın'),
        ('b', 'Belirtmek istemiyorum'),
        ]
    
    cinsiyet=models.CharField(choices=CİNSİYET_TABLOSU, max_length=11, default=CİNSİYET_TABLOSU[2][0])

    class Meta:
        verbose_name_plural = 'GDSC Başvuruları' 




class Basvuru5(models.Model):
    name = models.CharField(max_length=50,blank= True)  #blank = false, boş geçilememesini sağlar
    surname = models.CharField(max_length=30,blank= True)
    tckimlik = models.CharField(max_length=11 ,blank= True,unique=True) #eşsiz olmasını sağladım
    telefon = models.CharField(max_length=30 ,blank= True)
    tecrübe = models.CharField(max_length=50 ,blank= True)
    message = models.CharField(max_length=30,blank= True )
    #onay = models.BooleanField(verbose_name="Onay", default=False, blank=False)
    confirmed = models.BooleanField(verbose_name="Durum", default=False)

    posta = models.EmailField(blank=True) #boş geçilemez

    BOLUMLER =[

            ('SPO', 'Spor'),
            ('FEN', 'Fen Bilimleri'),
            ('MUH', 'Mühendislik'),
    ]
    bolum = models.CharField(max_length=3, choices=BOLUMLER,default=BOLUMLER[2][0])
    #seçimli modeller = bölümler - cinsiyet ----> Fen bilimleri veritabanında fen olarak tutulacak örneğin. 

    CİNSİYET_TABLOSU = [
        
        ('e','Erkek'), 
        ('h','Kadın'),
        ('b', 'Belirtmek istemiyorum'),
        ]
    
    cinsiyet=models.CharField(choices=CİNSİYET_TABLOSU, max_length=11, default=CİNSİYET_TABLOSU[2][0])

    class Meta:
        verbose_name_plural = 'GFC Başvuruları' 



    


    


    

