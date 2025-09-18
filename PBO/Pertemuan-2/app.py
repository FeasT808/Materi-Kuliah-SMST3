class Mahasiswa :
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def cetak_data(self) : 
        print(f"Nama Saya {self.nama} dan Usia Saya {self.umur} Tahun")


mhs = Mahasiswa("Muhammad Sumbul", 23)
mhs.cetak_data()