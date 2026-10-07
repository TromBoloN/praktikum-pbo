def judul(teks):
    print("\n" + "=" * 52)
    print(teks.center(52))
    print("=" * 52)


def subjudul(teks):
    print("\n" + "-" * 52)
    print(teks.center(52))
    print("-" * 52)

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
    
#AGREGASI: Deck menampung objek Kartu yang dibuat secara independen    
class Deck: 
    def __init__(self):
        self.daftar_kartu = []
    
    def tambah_kartu(self, kartu: Kartu):
        if isinstance(kartu, Kartu):
            self.daftar_kartu.append(kartu)
            print(f"Kartu {kartu.nama} berhasil ditambahkan ke deck.")
    
    def tampilkan_deck(self):
        if not self.daftar_kartu:
            print("Deck kosong.")
            return
        print("Daftar Kartu dalam Deck:")
        for idx, k in enumerate(self.daftar_kartu, 1):
            print(f"{idx}. {k.nama} - Tipe: {k.tipe}, Cost: {k.cost}, Dmg/Efek: {k.damage}")

#Superclass 
class Karakter:
    nama_game = "Roguelite Card Battle Simulator"
    
    def __init__(self, nama, health):
        # Protected attribute untuk nama dan darah karakter
        self._nama = nama
        self._health = health
        # Private attribute untuk id karakter
        self.__id_karakter = id(self)
     
    #Method yang bakal di override subclass   
    def status(self):
        print(f"Nama Karakter: {self._nama}")
        print(f"{self._nama} - Health: {self._health}")
        
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, nilai):
        if not isinstance(nilai, (int, float)):
            print(f"  Status      : Health harus berupa angka. Perubahan health {self._nama} dibatalkan.")
            return

        if nilai >= 0:
            self._health = nilai
            print(f"  Status      : Health {self._nama} berhasil diubah.")
        else:
            print(f"  Status      : Health tidak boleh negatif. Perubahan health {self._nama} dibatalkan.")

# Subclass 1
class Hero(Karakter):
    max_energy = 3
    total_hero = 0

    def __init__(self, nama, class_hero, health, block):
        # Memanggil konstruktor superclass
        super().__init__(nama, health)
        # Atribut spesifik hero
        self.class_hero = class_hero
        self.__block = block
        self.energy = Hero.max_energy
        
        # KOMPOSISI: Hero membuat dan memniliki objek Deck internal secara langsung
        self.deck = Deck()
        Hero.total_hero += 1

    #METHOD OVERRIDING: menggantikan logika status() dari superclass Karakter
    def status(self):
        print(f"[Hero] {self._nama}")
        print(f"  Class       : {self.class_hero}")
        print(f"  Health      : {self._health}")
        print(f"  Block       : {self.__block}")
        print(f"  Total Kartu : {len(self.deck.daftar_kartu)}")
        
    def gunakan_kartu(self, kartu: Kartu, target: 'Musuh'):
        if kartu in self.deck.daftar_kartu:
            if self.energy >= kartu.cost:
                self.energy -= kartu.cost
                target.terima_damage(kartu.damage)

                print(f"{self._nama} menggunakan {kartu.nama} pada {target._nama}.")
                print(f"  Sisa Energi: {self.energy}")
            else:
                print(f"{self._nama} tidak memiliki cukup energi untuk menggunakan {kartu.nama}.")
        else:
            print(f"{kartu.nama} tidak terdapat dalam deck {self._nama}.")

    @property
    def block(self):
        return self.__block

    @block.setter
    def block(self, nilai):
        if not isinstance(nilai, (int, float)):
            print(f"  Status      : Block harus berupa angka. Perubahan block {self._nama} dibatalkan.")
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


class Musuh(Karakter):
    tingkat_kesulitan = "Normal"
    total_musuh = 0

    def __init__(self, nama, aksi_musuh, health, intent_damage):
        super().__init__(nama, health)
        self.aksi_musuh = aksi_musuh
        self.__intent_damage = intent_damage
        Musuh.total_musuh += 1

    def status(self):
        print(f"[Musuh] {self._nama}")
        print(f"  Rencana Aksi: {self.aksi_musuh}")
        print(f"  Health      : {self._health}")
        print(f"  Intent Dmg  : {self.intent_damage}")
        
    def terima_damage(self, damage):
        if not isinstance(damage, (int, float)):
            print(f"  Status      : Damage harus berupa angka.")
            return
        if damage < 0:
            print(f"  Status      : Damage tidak boleh negatif.")
            return
        self._health -= damage
        if self._health < 0:
            self._health = 0
        print(f"{self._nama} menerima {damage} damage. Health sekarang: {self._health}")

    @property
    def intent_damage(self):
        return self.__intent_damage

    @intent_damage.setter
    def intent_damage(self, nilai):
        if not isinstance(nilai, (int, float)):
            print(f"  Status      : Intent damage harus berupa angka. Perubahan intent damage {self._nama} dibatalkan.")
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

# Uji inheritence
subjudul("UJI INHERITANCE")

print(f"Hero merupakan Karakter : {isinstance(ironclad, Karakter)}")
print(f"Musuh merupakan Karakter : {isinstance(cultist, Karakter)}")

print()

print("Hero memanggil method status() hasil overriding:")
ironclad.status()

print()

print("Musuh memanggil method status() hasil overriding:")
cultist.status()

subjudul("UJI RELASI ASSOCIATION")

ironclad.deck.tambah_kartu(strike)
ironclad.deck.tambah_kartu(defend)

print()
ironclad.deck.tampilkan_deck()

print()

print(f"Health Cultist sebelum : {cultist.health}")

ironclad.gunakan_kartu(strike, cultist)

print(f"Health Cultist sesudah : {cultist.health}")

subjudul("UJI RELASI AGGREGATION")

deck_baru = Deck()

deck_baru.tambah_kartu(strike)
deck_baru.tambah_kartu(defend)

print()
deck_baru.tampilkan_deck()

print()
print("Kartu Strike tetap dapat digunakan di luar Deck:")
strike.info_kartu()

subjudul("UJI RELASI COMPOSITION")

print(f"Deck milik {ironclad._nama} dibuat otomatis: {isinstance(ironclad.deck, Deck)}")
print(f"Jumlah kartu dalam deck: {len(ironclad.deck.daftar_kartu)}")

print()

print("Deck merupakan bagian dari objek Hero.")
ironclad.deck.tampilkan_deck()