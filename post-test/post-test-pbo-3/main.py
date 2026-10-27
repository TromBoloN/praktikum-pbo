from lib2to3.fixes import fix_print
from lib2to3.fixes import fix_print
from abc import ABC, abstractmethod

def judul(teks):
    print("\n" + "=" * 52)
    print(teks.center(52))
    print("=" * 52)


def subjudul(teks):
    print("\n" + "-" * 52)
    print(teks.center(52))
    print("-" * 52)

class Kartu(ABC):
    nama_game = "Slay the Spire Simulator"
    total_kartu_dibuat = 0
    kategori_game = "Deck-Building"

    def __init__(self, nama, tipe, cost, nilai):
        self.nama = nama
        self.tipe = tipe
        self.__cost = cost
        self._nilai = nilai
        Kartu.total_kartu_dibuat += 1

    def info_kartu(self):
        print(f"{self.nama}")
        print(f"  Tipe        : {self.tipe}")
        print(f"  Energy Cost : {self.__cost}")
        print(f"  Nilai Efek  : {self._nilai}")

    @abstractmethod
    def efek(self, pemilik, target): ...

    @abstractmethod
    def deskripsi(self): ...

    def mainkan(self, pemilik, target):
        if pemilik.energy < self.cost:
            print(f"Energi tidak mencukupi untuk {self.nama}.")
            return
        pemilik.energy -= self.cost
        self.efek(pemilik, target)

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
    def nilai(self):
        return self._nilai

    @nilai.setter
    def nilai(self, nilai):
        if not isinstance(nilai, (int, float)):
            print(f"  Status      : Nilai efek harus berupa angka. Perubahan {self.nama} dibatalkan.")
            return
        if nilai >= 0:
            self._nilai = nilai
            print("  Status      : Nilai efek berhasil diubah.")
        else:
            print("  Status      : Nilai efek tidak boleh negatif.")


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

    def __str__(self):
        return f"{self.nama} ({self.tipe}, cost {self.cost})"

    def __lt__(self, other):
        return self.cost < other.cost
    
class KartuAttack(Kartu):
    def __init__(self, nama, cost, damage):
        super().__init__(nama, "Serangan", cost, damage)

    def efek(self, pemilik, target):
        target.terima_damage(self._nilai)

    def deskripsi(self):
        return f"Beri {self._nilai} damage."

class KartuDefend(Kartu):
    def __init__(self, nama, cost, block):
        super().__init__(nama, "Pertahanan", cost, block)

    def efek(self, pemilik, target):
        pemilik.block += self._nilai
        print(f"{pemilik._nama} mendapat {self._nilai} block. Total block: {pemilik.block}")

    def deskripsi(self):
        return f"Dapat {self._nilai} block."

class KartuSpesial(Kartu):
    def __init__(self, nama, cost, energi_didapat, biaya_hp):
        super().__init__(nama, "Spesial", cost, energi_didapat)
        self.biaya_hp = biaya_hp          

    def efek(self, pemilik, target):
        pemilik.health = max(0, pemilik.health - self.biaya_hp)
        pemilik.energy += self._nilai
        print(f"{pemilik._nama} kehilangan {self.biaya_hp} HP dan mendapat {self._nilai} energi.")
        print(f"  Sisa HP: {pemilik.health} | Energi: {pemilik.energy}")

    def deskripsi(self):
        return f"Kehilangan {self.biaya_hp} HP, dapat {self._nilai} energi."

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
            print(f"{idx}. {k.nama} - Tipe: {k.tipe}, Cost: {k.cost}, Efek: {k.deskripsi()}")

class Karakter:
    nama_game = "Roguelite Card Battle Simulator"
    
    def __init__(self, nama, health):
        self._nama = nama
        self._health = health
        self.__id_karakter = id(self)
     
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

class Hero(Karakter):
    max_energy = 3
    total_hero = 0

    def __init__(self, nama, class_hero, health, block):
        super().__init__(nama, health)
        self.class_hero = class_hero
        self.__block = block
        self.energy = Hero.max_energy
        
        self.deck = Deck()
        Hero.total_hero += 1

    def status(self):
        print(f"[Hero] {self._nama}")
        print(f"  Class       : {self.class_hero}")
        print(f"  Health      : {self._health}")
        print(f"  Block       : {self.__block}")
        print(f"  Total Kartu : {len(self.deck.daftar_kartu)}")
        
    def gunakan_kartu(self, kartu: Kartu, target):
        if kartu not in self.deck.daftar_kartu:
            print(f"{kartu.nama} tidak terdapat dalam deck {self._nama}.")
            return
        kartu.mainkan(self, target)
        print(f"  Sisa Energi: {self.energy}")

    def terima_damage(self, damage):
        diserap = min(self.__block, damage)
        self.__block -= diserap
        sisa = damage - diserap
        self._health = max(0, self._health - sisa)
        print(f"{self._nama}: {diserap} diserap block, {sisa} mengenai health.")

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
            print("  Status      : Damage harus berupa angka.")
            return
        if damage < 0:
            print("  Status      : Damage tidak boleh negatif.")
            return
        self._health = max(0, self._health - damage)
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

class Relic:
    def __init__(self, nama, bonus_energi):
        self.nama = nama
        self._bonus_energi = bonus_energi

    def gunakan(self, pemilik):
        pemilik.energy += self._bonus_energi
        print(f"Relic {self.nama} aktif: {pemilik._nama} mendapat {self._bonus_energi} energi. Energi: {pemilik.energy}")

class Potion:
    def __init__(self, nama, jumlah_heal):
        self.nama = nama
        self.__jumlah_heal = jumlah_heal       
        self.sudah_dipakai = False

    def gunakan(self, pemilik):
        if self.sudah_dipakai:
            print(f"Potion {self.nama} sudah habis dipakai.")
            return
        pemilik.health = pemilik.health + self.__jumlah_heal
        self.sudah_dipakai = True
        print(f"Potion {self.nama} diminum: {pemilik._nama} pulih {self.__jumlah_heal} HP. HP: {pemilik.health}")


def pakai_item(item, pemilik):
    item.gunakan(pemilik)


# main
judul("Simulasi Deck Building Berbasis Giliran")

strike = KartuAttack("Strike", 1, 6)
defend = KartuDefend("Defend", 1, 5)
bloodletting = KartuSpesial("Bloodletting", 0, 2, 3)

ironclad = Hero("Ironclad", "Warrior", 80, 0)
silent = Hero("Silent", "Rogue", 70, 5)
cultist = Musuh("Cultist", "Menyerang", 50, 6)
jaw_worm = Musuh("Jaw Worm", "Menyerang/Bertahan", 40, 7)

subjudul("BUKTI ABSTRAKSI")
try:
    k = Kartu("X", "Tes", 1, 1)
except TypeError as e:
    print("Kartu tidak bisa diinstansiasi:", e)

subjudul("POLIMORFISME: SATU LOOP, TIGA JENIS KARTU")
for kartu in (strike, defend, bloodletting):
    ironclad.deck.tambah_kartu(kartu)

print()

for kartu in ironclad.deck.daftar_kartu:
    kartu.mainkan(ironclad, cultist)

print()
print(strike)

print()
print("Deck diurutkan berdasarkan cost:")
for k in sorted(ironclad.deck.daftar_kartu):
    print(f"  {k}")

subjudul("DUCK TYPING: RELIC DAN POTION")
lantern = Relic("Lantern", 1)
health_potion = Potion("Health Potion", 10)

for item in (lantern, health_potion):
    pakai_item(item, ironclad)
