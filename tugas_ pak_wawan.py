def TampilData(listdata):
  for x, y in listdata.items():
    print("NPM : "+str(x)+" Nama: "+y['name']+" Angkatan: "+str(y['year'])+
        " Alamat: "+y['address'])
    
DataMahasiswa = {
  1 : {
    "name" : "Emil",
    "year" : 2004,
    "address":"Lampung"
  },
  2 : {
    "name" : "Tobias",
    "year" : 2007,
    "address":"Jakarta"
  },
  3 : {
    "name" : "Linus",
    "year" : 2011,
    "address":"Palembang"
  }
}



def MasukanData(listdata):
  npm = int(input("Masukkan NPM yang akan update : "))
  if npm in listdata:
    nama = input("Masukkan nama baru: ")
    tahun = int(input("Masukkan anggkatan: "))
    alamat = input("Masukkan alamat baru: ")
    listdata[npm] = {"name": nama, "year": tahun, "address": alamat}
  else:
    print("NPM tidak ditemukan")
    
def MasukanDataBaru(listdata):
  npm = int(input("Masukkan NPM: "))
  nama = input("Masukkan nama: ")
  tahun = int(input("Masukkan angkatan: "))
  alamat = input("Masukkan alamat: ")
  listdata[npm] = {"name": nama, "year": tahun, "address": alamat}

def DeletData(listdata):
  npm = int(input("Masukkan NPM yang akan dihapus: "))
  if npm in listdata:
    del listdata[npm]
  else:
    print("NPM tidak ditemukan")




while True:
  TampilData(DataMahasiswa)
  print("\n=========================")
  print("Menu:")
  print("1. Tambah data baru")
  print("2. Hapus Data by NPM ")
  print("3. update data")
  print("4. Keluar")
  pilihan = int(input("Pilih menu: "))

  if pilihan   == 1:
    MasukanDataBaru(DataMahasiswa)
  elif pilihan == 2:
    DeletData(DataMahasiswa)
  elif pilihan == 3:
    MasukanData(DataMahasiswa)
  elif pilihan == 4:
    print("Program selesai. Terima kasih!")
    break
  else:
    print("Pilihan tidak valid")
