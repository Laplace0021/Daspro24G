from modul import pemilih, calon
def lakukan_voting():
    pelaku = input("Masukan ID pemilih")
    for p in pemilih.pemilih:
        if pemilih[p]["sudah_memilih"]==False:
            dipilih = input("Masukan ID calon")
            if dipilih in calon["id"]:
                pemilih.pemilih[pelaku]["sudah_memilih"==True]
                calon.calon[dipilih]["jumlah_suara"]+=1
            else:
                print("calon tidak ada")
        else:
            print("Pemilih tidak ada / sudah memilih")

def tampilkan_hasil():
    for x in calon:
        print (x)