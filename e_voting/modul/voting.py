from modul import pemilih, calon

def lakukan_voting():
    pelaku_id = input("Masukan ID pemilih: ")

    # Cari pemilih
    pemilih_terpilih = None
    for p in pemilih.pemilih:
        if p["id"] == pelaku_id:
            pemilih_terpilih = p
            break

    if pemilih_terpilih["sudah_memilih"]:
        print("Pemilih sudah memilih.")
        return

    dipilih_id = input("Masukan ID calon: ")

    # Cari calon
    calon_terpilih = None
    for c in calon.calon:
        if c["id"] == dipilih_id:
            calon_terpilih = c
            break

    # Lakukan voting
    calon_terpilih["jumlah_suara"] += 1
    pemilih_terpilih["sudah_memilih"] = True
    print("Voting berhasil!")

def tampilkan_hasil():
    for x in calon.calon:
        print(x)
