print('\n--- Mencetak nilai kelulusan ---')
#rata-rata nilai 70
def nilai_kelulusan(nilai):
    if nilai >= 80:
        return "lulus"
    else :
        return "gagal"

#untuk mencetak velue   
print(nilai_kelulusan(80))
print(nilai_kelulusan(60))
