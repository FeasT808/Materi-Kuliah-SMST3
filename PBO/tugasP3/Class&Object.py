import time 
class Tumbuhan:
    def __init__(self, nama, jenis, habitat, tinggi, cara_perkembangbiakan):
        self.nama = nama
        self.jenis = jenis
        self.habitat = habitat
        self.tinggi = tinggi
        self.cara_perkembangbiakan = cara_perkembangbiakan
    def tampilkan_info(self):
        print(f"Ini adalah tumbuhan dengan ciri-ciri : \n Nama :{self.nama} \n Jenis : {self.jenis} \n Habitat : {self.habitat} \n Tinggi : {self.tinggi} \n Cara Perkembangbiakan : {self.cara_perkembangbiakan}")   
    def fotosintesis(self):
        print(f"proses Fotosentesis pada tumbuhan {self.nama}:\n")
        time.sleep(3)
        print(f"1.Tumbuhan {self.nama}  menangkap energi cahaya matahari menggunakan klorofil yang ada pada daun.\n")
        time.sleep(3)
        print(f"2.Tumbuhan {self.nama} menyerap air (H2O) dari tanah melalui akar. \n")
        time.sleep(3)
        print(f"3.Tumbuhan {self.nama} mengambil karbon dioksida (CO2) dari udara melalui stomata di daun. \n")
        time.sleep(3)
        print(f"4. Tumbuhan {self.nama} menggunakan energi cahaya matahari untuk mengubah air (H2O) dan karbon dioksida (CO2) menjadi glukosa (C6H12O6) dan oksigen (O2). \n")
        time.sleep(3)
        print(f"Hasil dari fotosintesis pada tumbuhan {self.nama} digunakan untuk pertumbuhan dan perkembangan tumbuhan, serta menghasilkan oksigen yang dilepaskan ke udara. \n")


        
Padi = Tumbuhan("Padi", "rumput-rumputan", "Lahan Basah", "1,2m", "Dengan biji")
print("==================Informasi Tumbuhan =================")
Padi.tampilkan_info()
print("=====================================================")
print("==================Proses Fotosintesis =================")
Padi.fotosintesis()
print("=====================================================")


Jagung = Tumbuhan("Jagung", "rumput-rumputan", "Segala Habitat & Segala Jenis Tanah", "2,5m", "Dengan biji")
print("==================Informasi Tumbuhan =================")
Jagung.tampilkan_info()
print("=====================================================")
print("==================Proses Fotosintesis =================")    
Jagung.fotosintesis()
print("=====================================================")      
