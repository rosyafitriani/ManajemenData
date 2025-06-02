class Statistik:
    def __init__(self, pemilih_programmer, calon_programmer):
        self.pp = pemilih_programmer
        self.cp = calon_programmer

    def tampilkan_statistik(self):
        total = self.pp.jumlah_total()
        sudah = self.pp.jumlah_sudah()
        partisipasi = (sudah / total * 100) if total > 0 else 0

        print("Statistik Pemilu:")
        print(f"Total pemilih      : {total}")
        print(f"Sudah memilih      : {sudah}")
        print(f"Partisipasi       : {partisipasi:.2f}%")

        
        suara_max = max(self.cp.data, key=lambda c: c.get('jumlah_suara', 0))
        print(f"Pemimpin sementara : {suara_max['Nama']} ({suara_max.get('jumlah_suara', 0)} suara)")