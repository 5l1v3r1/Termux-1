import os,time,random,sys
def printz(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03) 
try:
    open(".setup", "r")
    print('Kurulumları Zaten Yapmışsınız Sizi Sonraki Aşamaya Geçiriyorum.')
    os.system('python asama1.py')
except:
       
    def main():
       try:
           os.system('clear')
           
           printz('Genel Kurulumlardan Başlayalım.')
           print('\n')
           printz('Kurulumda (Y/n) Yazısı Çıkarsa Y tuşuna basıp entera basın.')
           time.sleep(2)
           print('\n')
           printz('Termux Sürümün Güncelleniyor.')
           time.sleep(1)
           os.system('\n\n')
           os.system('pkg update')
           os.system('pkg upgrade')
           os.system('clear')
           printz('Pip Kuruluyor.')
           print('\n\n')
           os.system('pkg install pip')
           time.sleep(2)
           os.system('clear')
           printz('Requests Kuruluyor.')
           print('\n\n')
           os.system('pip install requests')
           os.system('clear')
           printz('PHP Kuruluyor.')
           time.sleep(2)
           print('\n\n')
           os.system('pip install php')
           os.system('clear')
           printz('WGET Paketi Kuruluyor.')
           time.sleep(2)
           os.system('pkg install wget')
           os.system('clear')
           printz('Python 2 Kuruluyor.')
           time.sleep(2)
           print('\n\n')
           os.system('pkg install python2')
           os.system('clear')
           printz('Genel Kurulumlar Tamamlandı.')
           os.system('touch .setup')
       except:
           print('Hata Kodu 202 Lütfen Yetkililere Bildirin.')
           
       
    try:
        tr = open(".skip", "r")
        main()
    except:
        os.system('clear')
        name = input('Sana Nasıl Hitap Etmeliyim Lütfen Adını Gir >> ')
        time.sleep(0.3)
        os.system('clear')
        printz('Merhaba '+name+'! Öncelikle Programımızı Kullandığın İçin Sana Teşekkür Etmek İsteriz.')
        print('\n')
        printz(name+' Sana Öncelikle Programımızı Açıklayayım.\nBu Program Termux ve Linuxa Yeni Başlayan Kullanıcılar İçin Üretildi ve Size Temel Eğitim ve Kurulumları Yapmayı Amaçlıyoruz.')
        print('\n')
        printz('Merak Etme Hepimiz Bir Yerden Başladık Ve Her Şeyi Teker Teker Öğrenmemiz Gerekti.')
        print('\n')
        printz('Bu Yüzden Bu Programda Yapılan Her Şey En Basite İndirgedik.')
        print('\n')
        os.system('touch .skip')
        skip = input('Atlamak İçin Enter Tuşuna Bas...')  
        os.system('clear')
        main()
