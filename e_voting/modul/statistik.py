from modul import pemilih, calon
def tampilkan_statistik():
    total_pemilih = len(pemilih.pemilih)
    print("total pemilih: ",total_pemilih)

    jumlah_memilih=0
    for x in pemilih.pemilih:
        if x["sudah_memilih"]==True:
            jumlah_memilih+=1
    print("jumlah yang sudah memilih ",jumlah_memilih)

    persentase = jumlah_memilih /total_pemilih*100
    print("persentase yang berpartisipasi ",persentase,end=" %.")

    if not calon.calon:
        print("Belum ada calon.")
        return
    
    tertinggi=[]
    for y in calon.calon:
        tertinggi.append(y["jumlah_suara"])
    maxim=max(tertinggi)
    for z in calon.calon:
        if z["jumlah_suara"]==maxim:
            print(f"calon dengan suara terbanyak {z}")
        