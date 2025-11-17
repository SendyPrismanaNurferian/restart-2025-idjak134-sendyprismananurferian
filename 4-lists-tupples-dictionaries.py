# List, Tupple,  and Dictionary are composite data type

# List
# List = Sebuah type data yang bisa menympan banyak nilai bersifat mutabble (dapat diubah)
print("Ini List")
myList = ["Jeruk", "Anggur", "Apple", 5000]
print(type(myList))
print(myList)
print(myList[1])
myList[0] = "Jeruk Bali" #Reassignment, overriding
print(myList)


# Tuple
# Tuple = Sebuah data type yang mirip dengan List, namun bersifat imutable (tidak bisa di ubah)
print("------------------------------------------------------")
print("Ini Tuple")
myTuple = ("Jeruk", "Anggur", "Apple", 6000)
print(type(myTuple))
print(myTuple)
print(myTuple[1])
# myTuple[1] "Anggur Merah" # reassignment, overriding akan menghasilkan error jika dijalankan!
# print(myTuple)


# Dictionary
# Dictionary = Type data seperti list namu indeks (key-pairs) dapat di custom dan bersifat mutable
print("------------------------------------------------------")
print("Ini Dictionary")
import json
myDict = {
    "buah1": "Jeruk",
    "buah2": "Anggur",
    "buah3": "Apel",
    "harga": "5000"
}

print(type(myDict))
print(myDict)
print(myDict["buah3"])
myDict["buah1"] = "Jeruk Bali"
print(myDict)

#biar rapi ke bawah
print(json.dumps(myDict, indent=4))


#########################
## CHALLENGE TIME ##
#########################

# Challenge 1
# Misalakan saya punya list myProgramingLang = ["Python", "Shell" , "JavaScript", "PHP", "Golang", "C++"]
# Bagaimana cara memaanggilnya dengan 1 pasang square bracket yaitu Golang dan C++

myProgramingLang = ["Python", "Shell" , "JavaScript", "PHP", "Golang", "C++"]

# Cara 1: Mulai dari indeks 4 sampai akhir list
# Ini adalah cara yang paling umum
print(myProgramingLang[4:])

# Cara 2: Mulai dari indeks 4 sampai sebelum indeks 6
print(myProgramingLang[4:6])

# Indeks negatif menghitung dari belakang list. "Golang" adalah elemen kedua dari belakang (indeks -2), dan "C++" adalah elemen terakhir (indeks -1).
print(myProgramingLang[-2:])

#Challenge 2
## 1. Definisikan dictionary
myComplexDict = {
    "name": "sendy prismana",
    "alamat": {
        "provinsi": "Jawa Timur",
        "kecamatan": "Sawahan",
        "desa": "Pekuningan",
        "RT": "01",
        "RW": "02"
    },
    "siblings": ["azizah", "anisa", "pramudita"]
}

# 2. Ambil semua data yang diperlukan ke variabel
nama = myComplexDict["name"]
kec = myComplexDict["alamat"]["kecamatan"]
desa = myComplexDict["alamat"]["desa"]
rt = myComplexDict["alamat"]["RT"]
rw = myComplexDict["alamat"]["RW"]

# 3. Ubah list saudara menjadi string, gabungkan dengan ", "
saudara_list = myComplexDict["siblings"]
saudara_str = ", ".join(saudara_list)

# 4. Gabungkan semua ke dalam f-string
output = f"Nama {nama}, alamat: {kec}, {desa} RT {rt}, RW {rw}. Saudara: {saudara_str}"

print(output)