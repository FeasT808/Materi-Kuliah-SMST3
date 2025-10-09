class Kendaraan:
  def __init__(self, merk, tahun, kapasitas_tangki):
    self.merk = merk
    self.tahun = tahun
    self.__kapasitas_tangki = kapasitas_tangki
    self.__odometer = 0

  def get_kapasitas_tangki(self):
    return self.__kapasitas_tangki

  def tambah_km(self, km):
    if km > 0:
      self.__odometer += km

  def deskripsi(self):
    return f"{self.merk} ({self.tahun}) - Odo: {self.__odometer} km, Tangki: {self.__kapasitas_tangki} L"

class MotorFadli(Kendaraan):
  def __init__(self, merk, tahun, kapasitas_tangki, cc, tipe_mesin):
    super().__init__(merk, tahun, kapasitas_tangki)
    self.cc = cc
    self.tipe_mesin = tipe_mesin


  def deskripsi(self):
    return f" {super().deskripsi()} | Motor {self.cc}cc | Mesin: {self.tipe_mesin}"
  
  def biaya_sewa_per_hari(self,hari):
    biaya_sewa_per_hari = 100000
    return biaya_sewa_per_hari * hari

Motor = MotorFadli("HONDA PCX", 2025, "25L", 155, "CVT")
Motor.tambah_km(420)
print(Motor.deskripsi())
print(f"Biaya sewa 4 hari : Rp {Motor.biaya_sewa_per_hari(4):,.0f}")