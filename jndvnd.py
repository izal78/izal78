def TampilData(listdata):
  for x, y in listdata.items():
    print("NPM : "+str(x)+" Nama: "+y['name']+" Angkatan: "+str(y['year'])+
        " Alamat: "+y['address'])

def TambahData(listdata):
  npm = int(input("Masukkan NPM: "))
  nama = input("Masukkan nama: ")
  tahun = int(input("Masukkan angkatan: "))
  alamat = input("Masukkan alamat: ")
  listdata[npm] = {"name": nama, "year": tahun, "address": alamat}

def UbahData(listdata):
  npm = int(input("Masukkan NPM yang akan diubah: "))
  if npm in listdata:
    nama = input("Masukkan nama baru: ")
    tahun = int(input("Masukkan anggkatan: "))
    alamat = input("Masukkan alamat baru: ")
    listdata[npm] = {"name": nama, "year": tahun, "address": alamat}
  else:
    print("NPM tidak ditemukan")

def HapusData(listdata):
  npm = int(input("Masukkan NPM yang akan dihapus: "))
  if npm in listdata:
    del listdata[npm]
  else:
    print("NPM tidak ditemukan")

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
while True:
  TampilData(DataMahasiswa)
  print("\n=========================")
  print("Menu:")
  print("1. Tambah data baru")
  print("2. Ubah data")
  print("3. Hapus data")
  print("4. Keluar")
  pilihan = int(input("Pilih menu: "))

  if pilihan   == 1:
    TambahData(DataMahasiswa)
  elif pilihan == 2:
    UbahData(DataMahasiswa)
  elif pilihan == 3:
    HapusData(DataMahasiswa)
  elif pilihan == 4:
    break
  else:
    print("Pilihan tidak valid")
