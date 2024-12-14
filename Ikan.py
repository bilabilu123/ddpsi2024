from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.warna = warna
        
    def cetak_ikan(self):
        super().cetak()
        print("jenis \t: ", self.jenis,
              "\nwarna \t: ", self.warna)
        
koi = Ikan("koi", "cacing", "air", "bertelur", "kohaku", "putih dan merah")
koi.cetak_ikan()

nila = Ikan("nila", "sayuran hijau", "air", "bertelur", "Oreochromis niloticus", "hitan dan putih")
nila.cetak_ikan()

