#clas induk
class Teknologi:
    def __init__(self, nama, tahun_ditemukan):
        self.__nama = nama
        self.__tahun_ditemukan = tahun_ditemukan

    def get_nama(self):
        return self.__nama

    def get_tahun_ditemukan(self):
        return self.__tahun_ditemukan

    def display_info(self):
        print(f"Nama: {self.__nama}")
        print(f"Tahun Ditemukan: {self.__tahun_ditemukan}")


class Gadget(Teknologi):
    def __init__(self, nama, tahun_ditemukan, jenis, harga):
        super().__init__(nama, tahun_ditemukan)
        self.__jenis = jenis
        self.__harga = harga

    def get_jenis(self):
        return self.__jenis

    def get_harga(self):
        return self.__harga

    def display_info(self):
        super().display_info()
        print(f"Jenis: {self.__jenis}")
        print(f"Harga: {self.__harga}")


class Software(Teknologi):
    def __init__(self, nama, tahun_ditemukan, platform, bahasa, versi):
        super().__init__(nama, tahun_ditemukan)
        self.__platform = platform
        self.__bahasa = bahasa
        self.__versi = versi

    def get_platform(self):
        return self.__platform

    def get_bahasa(self):
        return self.__bahasa

    def get_versi(self):
        return self.__versi

    def display_info(self):
        super().display_info()
        print(f"Platform: {self.__platform}")
        print(f"Bahasa: {self.__bahasa}")
        print(f"Versi: {self.__versi}")


class Smartphone(Gadget):
    def __init__(self, nama, tahun_ditemukan, jenis, harga, merk, ram):
        super().__init__(nama, tahun_ditemukan, jenis, harga)
        self.__merk = merk
        self.__ram = ram

    def get_merk(self):
        return self.__merk

    def get_ram(self):
        return self.__ram

    def display_info(self):
        super().display_info()
        print(f"Merk: {self.__merk}")
        print(f"RAM: {self.__ram} GB")


def main():
    while True:
        print("\n=== Aplikasi Informasi Teknologi ===")
        print("1. Informasi Smartphone")
        print("2. Informasi Software")
        print("3. Keluar")

        pilihan = input("Masukkan nomor pilihan (1/2/3): ")
        
        if pilihan == "1":
            merk = input("Masukkan merk Smartphone: ")
            tahun_ditemukan = int(input("Masukkan tahun ditemukan: "))
            jenis = input("Masukkan jenis Smartphone: ")
            harga = float(input("Masukkan harga Smartphone: "))
            ram = int(input("Masukkan RAM Smartphone (GB): "))

            smartphone = Smartphone(merk, tahun_ditemukan, jenis, harga, merk, ram)
            smartphone.display_info()

        elif pilihan == "2":
            platform = input("Masukkan platform Software: ")
            tahun_ditemukan = int(input("Masukkan tahun ditemukan: "))
            bahasa = input("Masukkan bahasa pemrograman Software: ")
            versi = float(input("Masukkan versi Software: "))

            software = Software("Software", tahun_ditemukan, platform, bahasa, versi)
            software.display_info()

        elif pilihan == "3":
            print("Terima kasih! Keluar dari aplikasi.")
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan nomor pilihan yang benar.")
            
       
if __name__ == "__main__":
    main()
    

