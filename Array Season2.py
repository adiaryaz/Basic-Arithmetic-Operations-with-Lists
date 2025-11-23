# def MenuUtama(inputMenu, nama):
#     if (inputMenu == 1):
#         print('Ini Menu Beranda, Halo ' + nama)
#     if (inputMenu == 2):
#         print('Ini Menu About, Halo ' + nama)
#     if (inputMenu == 3):
#         print('Ini Menu Help, Halo ' + nama)


# inputMenu = int(input())
# nama = str(input())

# MenuUtama(inputMenu, nama)

def aritmatika(angka1, angka2):
    hasilKurang = angka1 - angka2
    hasilTambah = angka1 + angka2
    hasilKali = angka1 * angka2
    return hasilKurang, hasilTambah, hasilKali
hasilAritmatika = [0,0,0]
inputUser = []
inputUser.append(int(input()))
inputUser.append(int(input()))
hasilAritmatika[0], hasilAritmatika[1], hasilAritmatika[2]= aritmatika(inputUser[0],inputUser[1])

print(hasilAritmatika)






# def MenulisdiPapan(jumlahIterasi): # Ini Prosedur 3
#     for i in range(jumlahIterasi):
#         print('Saya tidak akan mengulangi kesalahannya lagi ' + str(i+1))


# def Sambutan(jenis, nama): # Ini Prosedur 2
#     if (jenis == 'UlangTahun'):
#         print('Selamat Ulang Tahun, ' + nama)
#     else:
#         print('Halo, ' + nama)

# def MenuPsikologi(): # Ini Prosedur 1
#     print('Apakah Anda sering  di rumah aja?')
#     print('1. Ya')
#     print('2. Tidak')
#     print('Pilihan Anda: ')
#     inputUser = int(input())
#     if(inputUser == 1):
#         print('Anda Introvert')
#     else:
#         print('Anda Ekstrovert')

# def kalkulator(angka1, kondisi, angka2): # Ini Fungsi
#     if (kondisi == 'kali'):
#         hasil = angka1 * angka2
#     if (kondisi == 'kurang'):
#         hasil = angka1 - angka2
#     if (kondisi == 'tambah'):
#         hasil = angka1 + angka2
#     if (kondisi == 'bagi'):
#         hasil = angka1 / angka2
#     return hasil



# def Menu():
#     print('Ini adalah menu pilihan:');
#     print('1. Menu Psikolog') 
#     print('2. Sambutan')
#     print('3. Menu Kalkulator')
#     print('4. Menu Menulis di Papan')
#     print('Pilih menu: ')
#     inputUser = int(input())
#     if(inputUser == 1):
#         MenuPsikologi()
#     if(inputUser == 2):
#         Sambutan('UlangTahun', 'Beny')
#     if(inputUser == 3):
#         angka1 = int(input())
#         kondisi = str(input())
#         angka2 = int(input())
#         hasil = kalkulator(angka1, kondisi, angka2)
#         print('Hasil Kalkulator = ' + str(hasil))
#     if(inputUser == 4):
#         MenulisdiPapan(int(input()))

# Menu()














        
