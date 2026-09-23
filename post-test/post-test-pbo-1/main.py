def judul(teks):
    print("\n" + "=" * 52)
    print(teks.center(52))
    print("=" * 52)


def subjudul(teks):
    print("\n" + "-" * 52)
    print(teks.center(52))
    print("-" * 52)

#Tema Lengkap: Sistem Simulasi Permainan Kartu Deck-Building Berbasis Giliran
class Kartu:
    nama_game = "Slay the Spire Simulator" 
    total_kartu_dibuat = 0
    kategori_game = "Deck-Building"

    def __init__(self, nama, tipe, cost, damage):
        self.nama = nama
        self.tipe = tipe
        self.__cost = cost
        self.__damage = damage
        Kartu.total_kartu_dibuat += 1

    def info_kartu(self):
        print(f"{self.nama}")
        print(f"  Tipe        : {self.tipe}")
        print(f"  Energy Cost : {self.__cost}")
        print(f"  Nilai Efek  : {self.__damage}")

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, nilai):
        if not isinstance(nilai, (int, float)):
            print(f"  Status      : Energy cost harus berupa angka. Perubahan cost {self.nama} dibatalkan.")
            return

        if nilai >= 0:
            self.__cost = nilai
            print("  Status      : Energy cost berhasil diubah.")
        else:
            print(f"  Status      : Energy cost tidak boleh negatif. Perubahan cost {self.nama} dibatalkan.")

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, nilai):
        if not isinstance(nilai, (int, float)):
            print(f"  Status      : Nilai damage harus berupa angka. Perubahan damage {self.nama} dibatalkan.")
            return

        if nilai >= 0:
            self.__damage = nilai
            print("  Status      : Nilai damage berhasil diubah.")
        else:
            print("  Status      : Nilai damage tidak boleh negatif.")

    @classmethod
    def total_kartu(cls):
        print(f"Total Kartu Terdaftar : {cls.total_kartu_dibuat}")

    @staticmethod
    def validasi_cost(cost):
        if not isinstance(cost, (int, float)):
            return False

        if cost < 0:
            return False
        return True


class Hero:
    nama_game = "Slay the Spire Simulator"
    max_energy = 3
    total_hero = 0

    def __init__(self, nama, class_hero, health, block):
        self.nama = nama
        self.class_hero = class_hero
        self.__health = health
        self.__block = block
        Hero.total_hero += 1

    def status(self):
        print(f"{self.nama}")
        print(f"  Class       : {self.class_hero}")
        print(f"  Health      : {self.__health}")
        print(f"  Block       : {self.__block}")

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, nilai):
        if not isinstance(nilai, (int, float)):
            print(f"  Status      : Health harus berupa angka. Perubahan health {self.nama} dibatalkan.")
            return

        if nilai >= 0:
            self.__health = nilai
            print("  Status      : Health pemain berhasil diubah.")
        else:
            print(f"  Status      : Health tidak boleh negatif. Perubahan health {self.nama} dibatalkan.")

    @property
    def block(self):
        return self.__block

    @block.setter
    def block(self, nilai):
        if not isinstance(nilai, (int, float)):
            print(f"  Status      : Block harus berupa angka. Perubahan block {self.nama} dibatalkan.")
            return

        if nilai >= 0:
            self.__block = nilai
            print("  Status      : Block berhasil diubah.")
        else:
            print("  Status      : Block tidak boleh negatif.")

    @classmethod
    def info_hero(cls):
        print(f"Nama Game           : {cls.nama_game}")
        print(f"Maksimal Energi     : {cls.max_energy}")
        print(f"Total Hero        : {cls.total_hero}")

    @staticmethod
    def validasi_nama_hero(nama):
        if not isinstance(nama, str):
            return False

        if nama.strip() == "":
            return False
        return True


class Musuh:
    nama_game = "Slay the Spire Simulator"
    tingkat_kesulitan = "Normal"
    total_musuh = 0

    def __init__(self, nama, aksi_musuh, health, intent_damage):
        self.nama = nama
        self.aksi_musuh = aksi_musuh
        self.__health = health
        self.__intent_damage = intent_damage
        Musuh.total_musuh += 1

    def info_musuh(self):
        print(f"{self.nama}")
        print(f"  Rencana Aksi: {self.aksi_musuh}")
        print(f"  Health      : {self.__health}")
        print(f"  Intent Dmg  : {self.__intent_damage}")

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, nilai):
        if not isinstance(nilai, (int, float)):
            print(f"  Status      : Health harus berupa angka. Perubahan health {self.nama} dibatalkan.")
            return

        if nilai >= 0:
            self.__health = nilai
            print("  Status      : Health musuh berhasil diubah.")
        else:
            print(f"  Status      : Health musuh tidak boleh negatif. Perubahan health {self.nama} dibatalkan.")

    @property
    def intent_damage(self):
        return self.__intent_damage

    @intent_damage.setter
    def intent_damage(self, nilai):
        if not isinstance(nilai, (int, float)):
            print(f"  Status      : Intent damage harus berupa angka. Perubahan intent damage {self.nama} dibatalkan.")
            return

        if nilai >= 0:
            self.__intent_damage = nilai
            print("  Status      : Intent damage berhasil diubah.")
        else:
            print("  Status      : Intent damage tidak boleh negatif.")

    @classmethod
    def info_total_musuh(cls):
        print(f"Total Musuh Aktif   : {cls.total_musuh}")
        
    @staticmethod
    def validasi_damage(damage):
        if not isinstance(damage, (int, float)):
            return False

        return damage >= 0

# main
judul("Simulasi Deck Building Berbasis Giliran")

# Buat minimal 2 objek untuk tiap class.
strike = Kartu("Strike", "Serangan", 1, 6)
defend = Kartu("Defend", "Pertahanan", 1, 5)

ironclad = Hero("Ironclad", "Warrior", 80, 0)
silent = Hero("Silent", "Rogue", 70, 5)

cultist = Musuh("Cultist", "Menyerang", 50, 6)
jaw_worm = Musuh("Jaw Worm", "Menyerang/Bertahan", 40, 7)

# Uji Method Class
subjudul("UJI CLASS METHOD")
Kartu.total_kartu()
print()
Hero.info_hero()
print()
Musuh.info_total_musuh()

# Uji Instance Method
subjudul("UJI INSTANCE METHOD")
print("KARTU")
strike.info_kartu()
print()
defend.info_kartu()

print("\nPEMAIN")
ironclad.status()
print()
silent.status()

print("\nMUSUH")
cultist.info_musuh()
print()
jaw_worm.info_musuh()

# Uji Setter & Validasi Data (Valid & Tidak Valid)
subjudul("UJI SETTER & VALIDASI DATA")
print("Uji 1 - Health Ironclad valid")
print()
print(f"  Sebelum     : {ironclad.health}")
ironclad.health = 75
print(f"  Sesudah     : {ironclad.health}\n")

print("Uji 2 - Health Silent tidak valid")
print()
print(f"  Sebelum     : {silent.health}")
silent.health = -10
print(f"  Sesudah     : {silent.health}\n")

print("Uji 3 - Cost Strike tidak valid")
print()
print(f"  Sebelum     : {strike.cost}")
strike.cost = -2
print(f"  Sesudah     : {strike.cost}\n")

print("Uji 4 - Cost Defend salah tipe data")
print()
print(f"  Sebelum     : {defend.cost}")
defend.cost = "dua"
print(f"  Sesudah     : {defend.cost}")

# Uji Static Method
subjudul("UJI STATIC METHOD")
print(f"Nama hero 'Ironclad' valid              : {Hero.validasi_nama_hero('Ironclad')}")
print(f"Nama hero 123 valid                     : {Hero.validasi_nama_hero(123)}")
print(f"Cost kartu -1 valid                     : {Kartu.validasi_cost(-1)}")
print(f"Cost kartu 2 valid                      : {Kartu.validasi_cost(2)}")
print(f"Cost kartu 'dua' valid                  : {Kartu.validasi_cost('dua')}")
print(f"Damage musuh -5 valid                   : {Musuh.validasi_damage(-5)}")
print(f"Damage musuh 10 valid                   : {Musuh.validasi_damage(10)}")
print(f"Damage musuh 'besar' valid              : {Musuh.validasi_damage('besar')}")
