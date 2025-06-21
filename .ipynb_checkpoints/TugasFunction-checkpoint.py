def reverse_per_kata(kalimat):
    words = kalimat.split() # mengubah str menjadi list [kata1,kata2,kata3,...]
    result=[]  #membuat list kosong untuk mempertahankan urutan dari kata setelah direverse
    for word in words:
        reverse = word[::-1] #mereverse kata  ([start:stop:step]), start dan end kita pakai ":"karena ingin mereverse seluruh kata dan step "-1" untuk memulai dari belakang
        result.append(reverse) #kata yang sudah di reverse di masukan kedalam list result
    return ' '.join(result)   #menyatukan semua isi dari list result dengan pemisah " "(spasi)

def urutan_kalimat(kalimat,urutan): 
    urut = kalimat.split()  #string ke list , jadi memiliki indeks perkata
    rankata = []      #menyediakan list kosong untuk hasil
    for x in urutan :     # looping untuk memanggil kata berdasarkan urutan yang diinginkan
        rankata.append(urut[x-1])  #memasukan hasilnya kedalam list yang sudah disediakan, x dikurangi 1, karena indeks dimulai dari 1
    return " ".join(rankata)   #mengubah list menjadi string dengan spasi sebagai pemisah 

def ganti_vokal(kalimat,opsi):
    kata = kalimat.split()  #kata = list dari kalimat
    result=[]          #menyediakan list kosong 
    if opsi ==1:         #opsi 1 jika huruf vocal kecil
        for x in kata:   #untuk setiap kata yang ada di list kata
            ubah =x.replace('a','4').replace('i','1').replace('u','|_|').replace('e','3').replace('o','0')    #mengubah vocal jadi simbol
            result.append(ubah)    #memasukan hasil kata yang sudah diubah
    elif opsi==2:       #opsi 2 jika guruf vokal kapital
        for x in kata:  #untuk semua kata didalam list kata
            ubah =x.replace('A','4').replace('I','1').replace('U','|_|').replace('E','3').replace('O','0')  #mengubah huruf vocal menjadi simbol 
            result.append(ubah) #memasukan hasil kata yang sudah diubah
    return " ".join(result) #mengubah list menjadi string dengan spasi sebagai pemisah 


print(reverse_per_kata("AKU CINTA KAMU"))
print(urutan_kalimat("HARI INI SEDANG BELAJAR PYTHON", [5,1,4,3,2]))
print(ganti_vokal("Aku Cinta Kamu",1))
print(ganti_vokal("Aku Cinta Kamu",2))