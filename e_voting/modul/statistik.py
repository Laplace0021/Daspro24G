from modul import pemilih, calon
def tampilkan_statistik():
    total_pemilih = len(pemilih.pemilih)
<<<<<<< HEAD
    print("total pemilih: ",total_pemilih)
=======
    print("total pemilih ",total_pemilih)
>>>>>>> fccab66a4e68cd483cc00c6c4292eccf06d22678

    jumlah_memilih=0
    for x in pemilih.pemilih:
        if x["sudah_memilih"]==True:
            jumlah_memilih+=1
    print("jumlah yang sudah memilih ",jumlah_memilih)

<<<<<<< HEAD
    persentase = jumlah_memilih /total_pemilih*100
    print("persentase yang berpartisipasi ",persentase,end=" %.")

    if not calon.calon:
        print("Belum ada calon.")
        return
    
=======
    persentase = (jumlah_memilih/total_pemilih)*100
    print("persentase yang berpartisipasi ",persentase,end=" %.")

>>>>>>> fccab66a4e68cd483cc00c6c4292eccf06d22678
    tertinggi=[]
    for y in calon.calon:
        tertinggi.append(y["jumlah_suara"])
    maxim=max(tertinggi)
    for z in calon.calon:
        if z["jumlah_suara"]==maxim:
            print(f"calon dengan suara terbanyak {z}")
        