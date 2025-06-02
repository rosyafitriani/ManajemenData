class CalonProgrammer:
    def __init__(self, data):
        self.data = data
        
    def tampil_calon(self):
        print("Daftar Calon Ketua: ")
        for c in self.data:
            print(f"{c['id']} - {c['Nama']} (Visi: {c['Visi']}) - Suara: {c.get('Jumlah Suara', 0)} ")
            
    def Validasi_id(self, calon_id):
        for c in self.data:
            if c['id'] == calon_id:
                return c
        return None
    
    def tambah_suara(self, calon_id):
        calon = self.validasi_id(calon_id)
        if calon:
            calon['Jumlah Suara'] = calon.get('Jumlah Suara', 0) + 1

    def tampilkan_hasil(self):
        print("Hasil Voting Sementara:")
        self.tampil_calon()