def mahasiswa_input(data1, data2, nomer):
    while True:
        data1.append(input('Masukan %s mahasiswa : '%data2))
        if len(data1[i]) == nomer:
            break
        else:
            data1.pop(i)
            continue

i = 0
nama=[]
nim=[]
tugas=[]
uts=[]
uas=[]
nilaiakhir=[]

while True:
    s_nama = input('Masukan Nama : ')
    nama.append(s_nama)
    s_nim = input('Masukan Nim : ')
    nim.append(s_nim)
    i_tugas = input('Masukan Nilai Tugas : ')
    tugas.append(i_tugas)
    i_uts = input('Masukan Nilai Uts : ')
    uts.append(i_uts)
    i_uas = input('Masukan Nilai Uas : ')
    uas.append(i_uas)
    i_nilaiakhir = (int(i_tugas)*0.30)+(int(i_uts)*0.35)+(int(i_uas)*0.35)
    nilaiakhir.append(i_nilaiakhir)
    
    more = ""
    while more!= "y" and more!= "t":
     more = input("Tambah Data (y/t)? : ")
    i+1
    if more=="t":
        break

print('                                             DATA MAHASISWA                                       ')
print('==================================================================================================')
print('|    No.    |    Nama    |    Nim    |    Tugas   |    UTS    |     UAS    |     Nilai Akhir     |')
print('==================================================================================================')
for data in range(len(nim)):
    print('|    ',data+1,'    |  ',nama[data],'  | ',nim[data],'   |   ',tugas[data],'     |  ',uts[data],'     |   ',uas[data],'     |  ',nilaiakhir[data],'            |')