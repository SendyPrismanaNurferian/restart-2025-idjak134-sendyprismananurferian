print("Hanya Latihan Kelas Data")

#Float (Bilangan Pecahan/Irasional)/Desimal
myValue = 3.99
print("Hasil Float")
print(myValue)
print(type(myValue))
print("===============================")

#String (Alphabet)
myString = "Sendy Prismana Nurferian"
print("Hasil String")
print(myString)
print(type(myString))
print("===============================")

#Interger (Bilangan Bulat)
myInterger = 100
print("Hasil Interger")
print(myInterger)
print(type(myInterger))
print("===============================")

#Bolean (True False)
myBoolean = False
print("Hasil Bolean")
print(myBoolean)
print(type(myBoolean))
print("===============================")

#Complex Variable = Imaginer Data
myImagine = 1j
print("Hasil Imaginer")
print(myImagine)
print(type(myImagine))
print("===============================")



# Math Operations
print("Hasil Math Operations")
num1 = 100
num2 = 5

print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)
print(num1 % num2) #sisa pembagian
print("===============================")

# Variable type conversion. From integer to string
print("Hasil Variable type conversion. From integer to string")
num1 = 10
num2 = 5
strNum1 = str(num1)
strNum2 = str(num2) + " ="

print(strNum1 + " + " + strNum2, num1 + num2)
print(strNum1 + " - " + strNum2, num1 - num2)
print(strNum1 + " * " + strNum2, num1 * num2)
print(strNum1 + " / " + strNum2, num1 / num2)
print(strNum1 + " % " + strNum2, num1 % num2) #sisa bagi


print("Converting num1 from "+ str(type(num1)) + " to "+ str(type(strNum1)))
 
# Refactoring the code
typeNum1 = str(type(num1))
typeStrNum1 = str(type(strNum1))
print(f"Converting num1 from {typeNum1} to {typeStrNum1}")