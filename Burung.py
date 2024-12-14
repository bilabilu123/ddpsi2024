from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna,):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.warna = warna

    def cetak_burung(self):
        super().cetak()
        print("jenis \t: ", self.jenis,
              "\nwarna \t: ", self.warna)
        
merpati = Burung("merpati", "biji-bijian", "darat", "bertelur", "columbidae", "putih")
merpati.cetak_burung()

kaka_tua = Burung("kaka tua", "buah-buahan", "darat", "bertelur", "Cacatua alba", "putih")
kaka_tua.cetak_burung()