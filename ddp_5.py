#Buat variabel list dengan velue, [nama kendaraan, jenis kendaraan, cc kendaraan, warna kendaraan, roda kendaaran]
#Tambahkan dari list tersebut dibelakang dengan velue, [harga kendaraan, tipe kendaraan]
#Tambhakan setelah jenis kendaraan dengan velue [merk kendaraan]

kendaraan = ["beat","motor","200cc","biruputih","2"]

#proses append 1 (harga kendaraan)
kendaraan.append ("20.000.000")

#proses append 2 (tipe kendaraan)
kendaraan.append ("matic")

#cetak nilai kendaraan (setelah perubahan)
print(kendaraan)

#sisipkan nilai untuk (tipe kendaraan)
kendaraan.insert (2,"honda")

#cetak hasil (list akhirnya)
print(kendaraan)
