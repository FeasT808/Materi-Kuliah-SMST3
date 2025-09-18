class Kelelawar:
    def __init__(self, mulut, sayap, bulu, telinga, mata, kaki):
        self.mulut = mulut
        self.sayap = sayap
        self.bulu = bulu
        self.telinga = telinga
        self.mata = mata 
        self.kaki = kaki
    def ini_kelelawar(self):
        print(f"Ini adalah kelelawar dengan ciri-ciri : Mulut :{self.mulut} \n Sayap : {self.sayap} \n Bulu : {self.bulu} \n Telinga : {self.telinga} \n Mata : {self.mata} \n Kaki : {self.kaki}")

Klwr = Kelelawar("Pendek", 2, "Tebal", 2, "Kecil", "Ber-cakar")
Klwr.ini_kelelawar()