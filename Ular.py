from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun,):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun
    def cetak_ular(self):
        super().cetak()
        print("Design \t: ", self.design,
              "\nracun \t: ", self.racun)
        
anaconda = Ular("python", "kambing", "darat", "bertelur", "zigzag", "tidak berbisa")
anaconda.cetak_ular()

cobra = Ular("cobra", "burung", "darat", "bertelur", "zigzag", "berbisa")
cobra.cetak_ular()