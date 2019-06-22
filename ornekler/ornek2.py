try:
    sayi1 = int(input('Bölünecek sayıyı giriniz'))
    sayi2 = int(input('Bölecek sayıyı giriniz'))
    # sonuc = sayi1/sayi2
    # print('işlem sonucu', sonuc)
except ValueError as exp:
    print('işlem hatası',exp)
else:
    try:
        print(sayi1/sayi2)
    except ZeroDivisionError:
        print('sayi 0 değerine bölünemez')
finally:
    print('bittie')