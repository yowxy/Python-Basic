# x = 'Dicoding'
# print(x[2:])

# name = "Perseus Evans"
# print("Nama saya %s" % (name))

# angka = 1 + 1
# print(angka)

# x = {1,2,7,2,3,13,3}
# print(x)

# kata = 'dicoding'
# kata = kata.upper()
# print(kata)
# string = "Ayo belajar Coding di Dicoding"
# print(string.replace("Coding", "Python"))

# x = (5, 'program', 1+3j)
# x[1] = 'Dicoding'
# print(x)

# x = "Belajar" 
# y = "Python" 
# result = x > y 
# print(result) 


# print("Selamat datang dalam program Python!\n")
# print("Silakan masukkan data diri Anda.")
# nama = input("Masukkan nama Anda: ")
# tahun_lahir = input("Masukkan tahun lahir Anda: ")
# umur = 2023 - int(tahun_lahir)
 
# print(f"Selamat datang {nama} dalam program Python, per 2023 umur Anda adalah {umur} tahun.\n")
# print("Terima kasih telah menggunakan program Python!")


## cara ke satu
# a = 6
# b = 9
 
# result = a + b
# print(result)

## cara ke dua

# a = 10
# b = 5

# print(a+b);

# for i in range(100):
#     print(i)


# Ayam = "Bertelur"
# Sapi = "Beranak"

# if Ayam and Sapi == "Bertelur" == "Beranak":
#     print("Ayam Bertelur")
#     print("Sapi beranak")
# else :
#     print("Ayam tidak bertelur")   



# for i in range(2,10,2):
#     print(i)
    

# nilai = 1

# while nilai <=10:
#     print(nilai)
#     nilai +=1

# for i in range(1,5):
#     for k in range(1,3):
#         print(i,k)


# perulangan berbasis break
# for huruf in "Dicoding":
#     if huruf =="":
#         break
#     print("Huruf saat ini:{}".format(huruf))

# numbers = [2,3,4,5,6,7,8,9]

# for a in numbers:
#     if a == 7:
#         print("Hello world")
#         break
#     else:
#         print("Angka tidak ditemukan")

# harga = 3000

# while harga<4000:
#     print("Hello world")
#     harga+=1
# else:
#     print("nt nt")

# n = 20
# while n > 0:
#     n = n - 1
#     if n == 7:
#         break
#     print(n)
#     print("Hasil nya adalah")
# else:
#     print("Loop selesai")

# x = 10

# if x > 5:
#     print("Hello World")
# else:
#     print("Nilai x tidak memenuhi kondisi")


# angka = [1, 2, 3, 4,5,6,7]
# pangkat = []
# for n in angka:
#   pangkat.append(n**2)
# print(pangkat)
# import array
# from ctypes import Array
# from turtle import clear


nilai=20
# print(nilai)

# import array

# x = array.array("i",[1, 2, 3, 4, 5])
# print(x)
# print(type(x))


# x = [1,2,3,4,5,6,6]
# y = len



# import numpy

# matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
# print(matriks)


# var_mat = [[1, 2, 3, 4, 5],
#            [6, 7, 8, 9, 10],
#            [11, 12, 13, 14, 15],
#            [16, 17, 18, 19, 20],
#            [21, 22, 23, 24, 25]]
           
# print(var_mat[1][2])



# var_mat = [[5, 0],
#           [1, -2]]
# def_mat = [[0 for j in range(2)] for i in range(2)]

# for i in range(len(var_mat)):
#   for j in range(len(var_mat[0])):
#     def_mat[i][j] = var_mat[i][j]*2

# print(def_mat)


# panjang = 5
# lebar = 10

# luas_persegi_panjang = panjang * lebar
# print(luas_persegi_panjang)



# def mencari_luas_persegi_panjang(panjang,lebar):
#     luas_persegi_panjang = panjang*lebar
#     return luas_persegi_panjang

# persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
# print(persegi_panjang_pertama)

# persegi_panjang_kedua = mencari_luas_persegi_panjang(4,15)
# print(persegi_panjang_kedua)


# def greeting(nama, pesan):
#     return "Halo, " + nama + "! " + pesan

# print(greeting("Dicoding", "Selamat pagi!"))
# print(greeting(pesan="Selamat sore!", nama="Dicoding"))

# class Mobil:
#     # Atribut
#     warna = "Merah dan biru"

# mobil_1 = Mobil()
# print(mobil_1.warna)


# class Motor :
#     Warna = "Hitam"
#     Keadaaan = "Mulus"
    
# Motor_2 = Motor()
# Motor_2.Warna ="Putih"
# Motor_2.Keadaaan = "Rusak parah "
# print(Motor_2.Warna)
# print(Motor_2.Keadaaan)   



# class Mobil:
#     def __init__(self, warna, merek, kecepatan):
#         self.warna = warna
#         self.merek = merek
#         self.kecepatan = kecepatan
        
# mobil_1 = Mobil("war","is","over")
# print(mobil_1.warna)
# print(mobil_1.merek)
# print(mobil_1.kecepatan)


# class Mobil:
#     def __init__(self, warna, merek, kecepatan):
#         self.warna = warna
#         self.merek = merek
#         self.kecepatan = kecepatan
    
#     def tambah_kecepatan(self):
#         self.kecepatan += 10

# mobil_1 = Mobil("Merah", "DicodingCar", 180)
# print(mobil_1.kecepatan)

# class MobilSport(Mobil):
#     def turbo(self):
#         self.kecepatan += 50

# # Kelas Mobil Dasar
# mobil_1 = Mobil("Merah", "DicodingCar", 160)
# print(mobil_1.kecepatan)

# # Kelas Mobil Sport
# mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
# print(mobil_sport_1.kecepatan)
# mobil_sport_1.turbo()
# print(mobil_sport_1.kecepatan)


# class Mobil:
#     def __init__(self, warna, merek, kecepatan):
#         self.warna = warna
#         self.merek = merek
#         self.kecepatan = kecepatan
    
#     def tambah_kecepatan(self):
#         self.kecepatan += 10


# class MobilSport(Mobil):
#     def turbo(self):
#         self.kecepatan += 50
    
#     def tambah_kecepatan(self):
#         super().tambah_kecepatan()
#         print("Kecepatan Anda meningkat! Hati-Hati!")

# # Kelas Mobil Sport
# mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
# mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
# print(mobil_sport_1.kecepatan)


# class Animal:
#     def __init__(self, name, age, species):
#         self.name = name
#         self.age = age
#         self.species = species
# class Cat(Animal):
#     def deskripsi(self):
#         return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
#     def suara(self):
#         return "meow!"
      
# myCat = Cat("Neko",3,"Persian")
# myCat.deskripsi()
# myCat.suara()


# import numpy

# matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
# print(matriks)


# import matplotlib.pyplot as plt
 
# # Data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
 
# # Membuat plot garis
# plt.plot(x, y)
 
# # Menambahkan judul dan label sumbu
# plt.title("Contoh Plot Garis")
# plt.xlabel("Sumbu X")
# plt.ylabel("Sumbu Y")
 
# # Menampilkan plot
# plt.show()


# import seaborn as sns
# import matplotlib.pyplot as plt
 
# # Contoh data
# tips = sns.load_dataset('tips')  # Memuat dataset tips dari Seaborn
 
# # Contoh plot histogram
# sns.histplot(tips['total_bill'], kde=True)
# plt.title('Histogram Total Bill')
# plt.xlabel('Total Bill')
# plt.ylabel('Frequency')
# plt.show()


# import json
 
# # contoh JSON:
# x = '{ "nama":"Buchori", "umur":22, "Kota":"New York"}'
 
# # parse  x:
# y = json.loads(x)
 
# print(y["Kota"])

# lulus = True 
# print("Dicoding Indonesia") if lulus else print("Python")
