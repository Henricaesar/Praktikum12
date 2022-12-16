from tabulate import tabulate
class UPB :
    def __init__(self):
        self.datamahasiswa = {
        'No':[],
        'Nama':[],
        'NIM':[],
        'Nilai Tugas':[],
        'Nilai UTS':[],
        'Nilai UAS':[],
        'Nilai Akhir':[]
    }

    def tambah (self,no):
        print("Silahkan Input Data Anda  ")
        nama = input("Masukan Nama Mahasiswa : ")
        nim = input("Masukan Nim Mahasiswa : ")
        tugas = int(input("Masukan Nilai Tugas Mahasiswa : "))
        uts = int(input("Masukan Nilai UTS Mahasiswa : "))
        uas = int(input("Masukan Nilai UAS Mahasiswa : "))
        nilaiAkhir = (0.3*tugas) + (0.35*uts) + (0.35*uas)
        
        self.datamahasiswa['No'].append(no)
        self.datamahasiswa['Nama'].append(nama)
        self.datamahasiswa['NIM'].append(nim)
        self.datamahasiswa['Nilai Tugas'].append(tugas)
        self.datamahasiswa['Nilai UTS'].append(uts)
        self.datamahasiswa['Nilai UAS'].append(uas)
        self.datamahasiswa['Nilai Akhir'].append(nilaiAkhir)
        print("Succes")
#Tampil
    def tampil(self):
        print('Tampilan Data Nilai Mahasiswa')
        print(tabulate(self.datamahasiswa,headers=['No','Nama','NIM','Nilai Tugas','Nilai UTS','Nilai UAS','Nilai Akhir'],tablefmt='fancy_grid'))
    
    def hapus(self,nama):
        if nama in self.datamahasiswa["Nama"]:
            namaIndex =self.datamahasiswa['Nama'].index(nama)
            del self.datamahasiswa['No'][namaIndex]
            del self.datamahasiswa['Nama'][namaIndex]
            del self.datamahasiswa['NIM'][namaIndex]
            del self.datamahasiswa['Nilai Tugas'][namaIndex]
            del self.datamahasiswa['Nilai UTS'][namaIndex]
            del self.datamahasiswa['Nilai UAS'][namaIndex]
            del self.datamahasiswa['Nilai Akhir'][namaIndex]
            print("Data Was Deleted")
        else:
            print("Data Was Not Found")
    
    
    def ubah(self, nama):
           # cek jika ada nama tersebut di dataMahasiswa
           if nama in self.datamahasiswa['Nama']:
               # cari posisi indexnya lalu disimpan di nimIndex
               namaIndex = self.datamahasiswa['Nama'].index(nama)
               print("Pilih data yang mau di edit : ")
           # peruntungan mengedit data dalam bentuk pilihan
           while True:
               editApa = int(input(
                   "(1) Nim, \n (2) Nama, \n (3) Nilai Tugas, \n (4) Nilai UTS, \n (5) Nilai UAS, \n (0) Save perubahan dan exit, \n "))
               print(" ")

               if editApa == 1:
                   # merubah Nim
                   newNim = int(input("Masukan Nim : "))
                   self.datamahasiswa['NIM'][namaIndex] = newNim
               elif editApa == 2:
                   # merubah Nama
                   newNama = input("Masukan Nama : ")
                   self.datamahasiswa['Nama'][namaIndex] = newNama
               elif editApa == 3:
                   # merubah Nilai Tugas & Nilai Akhir
                   newTugas = int(input("Masukan Nilai Tugas : "))
                   nilai_akhir = (newTugas * 30/100) + (self.datamahasiswa['UTS'][namaIndex] * 35/100) + (self.datamahasiswa['UAS'][namaIndex] * 35/100)
                   self.datamahasiswa['Tugas'][namaIndex] = newTugas
                   self.datamahasiswa['Nilai Akhir'][namaIndex] = nilai_akhir
               elif editApa == 4:
                   # merubah nilai UTS & Nilai Akhir
                   newUTS = int(input("Masukan Nilai UTS"))
                   nilai_akhir = (self.datamahasiswa['Tugas'][namaIndex] * 30/100) + (newUTS *35/100) + (self.datamahasiswa['UAS'][namaIndex] * 35/100)
                   self.datamahasiswa['UTS'][namaIndex] = newUTS
                   self.datamahasiswa['Nilai Akhir'][namaIndex] = nilai_akhir
               elif editApa == 5:
                   # merubah nilai UAS & nilai akhir
                   newUAS = int(input("Masukn Nilai UAS : "))
                   nilai_akhir = (self.datamahasiswa['Tugas'][namaIndex] * 30 / 100) + (self.datamahasiswa['UTS'][namaIndex] * 35 / 100) + (newUAS * 35 / 100)
                   self.datamahasiswa['UAS'][namaIndex] = newUAS
                   self.datamahasiswa['Nilai Akhir'][namaIndex]= nilai_akhir
               elif editApa == 0:
                   print("Perubahan data berhasil di simpan")
                   break
           else:
               print("Data tidak ditemukan")
no = 0
instanceUPB = UPB()
                    
loop = True
print("===================================================================")
print("             Selamat Datang Di Aplikasi Input Nilai Mahasiswa      ")
print("===================================================================")
print("                                   Menu                            ")
print("1. Tambah Data       ")
print("2. Tampilkan Data    ")
print("3. Hapus Data        ")
print("4. Ubah Nama dan Nilai mahasiswa   ")
print("0. Keluar            ")
print("======================================================================")


while loop:
    print("\n\n")
    menu = input("Masukan Menu : ")

    if menu == "1":
        while True :
            no +=1
            instanceUPB.tambah(no)
            tambahdata = input("Ingin Menambahkan Lagi ? (y/n) ")
            if tambahdata == "n":
                break
    elif menu == "2":
        instanceUPB.tampil()
        print(" ")
    elif menu == "3":
        print(tabulate(instanceUPB.datamahasiswa,headers=['No','Nama','NIM','Nilai Tugas','Nilai UTS','Nilai UAS','Nilai Akhir'],tablefmt='fancy_grid'))
        nama = input("Pilih Data Nama Yang Ingin Dihapus : ")
        instanceUPB.hapus(nama)
    elif menu == "4":
        print(tabulate(instanceUPB.datamahasiswa,headers=['No','Nama','NIM','Nilai Tugas','Nilai UTS','Nilai UAS','Nilai Akhir'],tablefmt='fancy_grid'))
        nama = input("Masukan Nama Yang Ingin Di Edit : ")
        print(" ")
        instanceUPB.ubah(nama)
    elif menu == "0":
        print("Terima Kasih Telah Menggunakan Program Ini")
        print("Thank You")
        loop = False
