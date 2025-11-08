class PomBensin:
    def __init__(self, jenis, liter):
        self.jenis, self.liter = jenis, liter
        self.harga = {"pertalite": 10000, "pertamax": 14000}

    def total(self):
        return self.liter * self.harga.get(self.jenis.lower(), 0)

    def struk(self):
        print(f"\n=== STRUK PEMBELIAN ===\nJenis : {self.jenis}\nLiter : {self.liter:.2f} L\nTotal : Rp{self.total():,.0f}\n========================\n")


class Main:
    def run(self):
        print("=== Program Pengisian Bensin ===")
        while True:
            jenis = input("Masukkan jenis bensin (Pertalite/Pertamax): ").strip().capitalize()
            if jenis not in ["Pertalite", "Pertamax"]:
                print("Jenis tidak valid!\n")
                continue
            try:
                liter = float(input("Masukkan jumlah liter (≥1): "))
                if liter < 1:
                    print("Minimal 1 liter!\n")
                    continue
            except ValueError:
                print("Input harus berupa angka!\n")
                continue

            PomBensin(jenis, liter).struk()
            if input("Isi lagi? (y/n): ").lower() != 'y':
                print("\nTerima kasih!")
                break


if __name__ == "__main__":
    Main().run()
