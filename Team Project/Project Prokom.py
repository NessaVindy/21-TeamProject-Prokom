import pandas as pd
df = pd.read_excel("Database1.xlsx")
df_baru = df.dropna()
print(df_baru)

def data(Jumlah_pinjaman, nomor):
    kode = (nomor) - 1
    data_harga = df_baru.iloc[kode, 3]
    data_bank = df_baru.iloc[kode, 1]
    persen_bunga = str(data_harga * 100) + "%" 
    bunga = data_harga * (Jumlah_pinjaman)
    jumlah_bulan = df_baru.iloc[kode, 2]
    jumlah_bulan1 = int(jumlah_bulan[:-6])
    jumlah_bulan2 = jumlah_bulan1*12
    angsuran = Jumlah_pinjaman/jumlah_bulan2
    data_1 = {'Nama Bank':  [data_bank], 'Jumlah Pinjaman' : [Jumlah_pinjaman],
        'Persen Bunga': [persen_bunga], 'Bunga Angsuran' : [bunga], 'Angsuran Pokok' :[angsuran]}
    return data_1

while True:
    try:
       nomor = int(input("Masukkan kode bank: "))
       if nomor <= 20 : 
        Jumlah_pinjaman = int(input("Masukkan Jumlah Pinjaman: "))
        data_asli = data(Jumlah_pinjaman, nomor)
        data_1 = pd.DataFrame(data_asli)
        data_1.to_csv("Output.csv", index= False)
        print(data_1)
        while True:
            validasi = input("Apakah Anda ingin mengajukan KPR lagi? (Ya/Tidak): ")
            if validasi.lower() == "ya":
                nomor = int(input("Masukkan kode bank: "))
                if nomor <= 20: 
                    Jumlah_pinjaman = int(input("Masukkan Jumlah Pinjaman: "))
                    data_2 = data(Jumlah_pinjaman, nomor)
                    data_2 = pd.DataFrame(data_2)
                    data_1 = data_1.append(data_2)
                    data_1.to_csv("Output.csv", index= False)
                    print(data_1)
            elif validasi.lower() == "tidak":
                break
        break     
       else:
           print("Please enter a valid number.")
           
    except ValueError:
       print("Please enter a valid number")

