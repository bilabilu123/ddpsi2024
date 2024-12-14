from Mahasiswa import *
from Dosen import *

m1 = Mahasiswa("Nabila Anggraini", "Wanita", 18, "SI", 1)
m2 = Mahasiswa("Budi Santoso", "Pria", 21,"Ti", 5)
d1 = Dosen('Sirojul Munir', "Pria", 43, "S.Si, M.Kom", "LLPM")
d2 = Dosen('Hendry Saptono', "Pria", 44, "S.Si, M.Kom", "LTSI")

d1.setGaji(12000000)
d2.setGaji(10000000)

m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()
