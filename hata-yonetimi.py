try:
    telno = input('Telefon numarsı giriniz.');
    print(int(telno))
except ValueError:
    print("işlem hatası")
    print("Lütfen geçerli bir sayı giriniz.")
except ZeroDivisionError:
    print("işlem hatası")
    print("sıfıra bölünme hatası")