class VotingSystem:
    def __init__(self, pemilih, calon):
        self.pemilih = pemilih
        self.calon = calon

    def voting(self):
        user_id = input("Masukkan ID Pemilih: ")
        pemilih = next((p for p in self.pemilih.data if p['id'] == user_id), None)

        if not pemilih:
            print("ID tidak ditemukan.")
            return

        if pemilih.get('sudah_memilih'):
            print("Anda sudah memilih sebelumnya.")
            return

        print("Pilih Calon:")
        for i, c in enumerate(self.calon.data, start=1):
            print(f"{i}. {c['Nama']}")

        try:
            pilihan = int(input("Masukkan nomor calon yang dipilih: "))
            if 1 <= pilihan <= len(self.calon.data):
                self.calon.data[pilihan - 1]['suara'] = self.calon.data[pilihan - 1].get('suara', 0) + 1
                pemilih['sudah_memilih'] = True
                print("Voting berhasil.")
            else:
                print("Nomor calon tidak valid.")
        except ValueError:
            print("Input tidak valid.")
