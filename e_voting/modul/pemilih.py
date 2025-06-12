pemilih=[]
def tambah_pemilih():#Struktur data: {"id": "PM001", "nama": "Ayu", "jurusan": "SI", "sudah_memilih": False}
    id = input("Masukan ID: ")
    nama = input("Masukan Nama: ")
    jurusan = input("Masukan Jurusan: ")
    return pemilih.append({"id":id,"nama":nama,"jurusan":jurusan,"sudah_memilih":False})
    