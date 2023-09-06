import random
import time

while True:
    sayı = random.randint(1, 10)
    can = 7

    while can > 0:
        tahmin = int(input("1 ile 10 arasında bir sayı giriniz: "))

        if tahmin == sayı:
            print("Doğru tahmin ettiniz! Kazandınız!")
            time.sleep(0.5)
            quit()  
        else:
            can -= 1
            print("Yanlış tahmin! Tekrar deneyin!")
            print(f"{can} canınız kaldı!")

        if can == 0:
            print("Kaybettiniz!! :(")

    Tercih = input("oyunu tekra oynamak istiyorsanız e/E istemiyorsanız h/H : ")
    if Tercih == "e" and "E":
        continue
    elif Tercih == "h" and "H":
        quit()
    

    

