nama_saya = str("Nama : Mohammad Fattahil Alim")
print(nama_saya, type(nama_saya))

NIM = str("NIM : 230441100141")
print (NIM, type(NIM))

print()

#meengonversi suhu derajat celcius menjadi derajat fahrenheit
celsius = int(input("masukkan suhu dalam derajat celcius : "))
fahrenheit = int((celsius*(9/5))+32)

print ("jika suhu celcius =",celsius,"derajat celcius","maka, suhu farenheit =",fahrenheit,"derajat fahrenheit")

print()

#mengonversi suhu derajat fahrenheit menjadi derajat celcius
fahrenheit = int(input("masukkan suhu dalam derajat fahrenheit : "))
celsius = int(((5*fahrenheit)-(5*32))/9)

print ("jika suhu fahrenheit =",fahrenheit,"derajat fahrenheit","maka, suhu celsius =",celsius,"derajat celcius")
