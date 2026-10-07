# POSTTEST 4 PBO 2026

**Nama:** Arif Abdurrahman Siddiq
**NIM:** 2509106064
**Kelas:** B1'25

## 1. Deskripsi Program

Program ini merupakan simulasi sederhana **deck-building card battle** berbasis giliran. Program menggunakan konsep Object-Oriented Programming (OOP) seperti:

* Class dan object
* Constructor
* Encapsulation
* Property
* Class method
* Static method
* Inheritance
* Method overriding
* Association
* Aggregation
* Composition

Class utama yang digunakan adalah `Kartu`, `Deck`, `Karakter`, `Hero`, dan `Musuh`.

---

# 2. Class Kartu

Class `Kartu` digunakan untuk membuat object kartu yang nantinya dapat dimasukkan ke dalam `Deck`.

## A. Constructor dan Atribut

```python
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
```

Penjelasan:

* `nama_game`, `total_kartu_dibuat`, dan `kategori_game` merupakan **class attribute**.
* `nama` dan `tipe` merupakan atribut object.
* `__cost` dan `__damage` menggunakan **private attribute**.
* `total_kartu_dibuat` bertambah setiap kali object `Kartu` dibuat.

## B. Method Info Kartu

```python
def info_kartu(self):
    print(f"{self.nama}")
    print(f"  Tipe        : {self.tipe}")
    print(f"  Energy Cost : {self.__cost}")
    print(f"  Nilai Efek  : {self.__damage}")
```

Method ini digunakan untuk menampilkan informasi dari sebuah kartu.

Atribut private tetap dapat digunakan di dalam class `Kartu` itu sendiri.

## C. Property Cost dan Damage

```python
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
```

Property digunakan agar atribut private `__cost` dan `__damage` dapat diakses dan diubah dengan validasi.

Validasi yang dilakukan adalah:

* Nilai harus berupa angka.
* Nilai tidak boleh negatif.

## D. Class Method dan Static Method

```python
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
```

`total_kartu()` merupakan **class method** karena menggunakan data milik class melalui `cls`.

`validasi_cost()` merupakan **static method** karena tidak membutuhkan data object maupun class. Method ini hanya digunakan untuk mengecek apakah nilai cost valid.

---

# 3. Class Deck

Class `Deck` digunakan untuk menyimpan beberapa object `Kartu`.

## A. Constructor

```python
class Deck:
    def __init__(self):
        self.daftar_kartu = []
```

`daftar_kartu` berupa list yang digunakan untuk menyimpan object-object `Kartu`.

## B. Menambahkan Kartu

```python
def tambah_kartu(self, kartu: Kartu):
    if isinstance(kartu, Kartu):
        self.daftar_kartu.append(kartu)
        print(f"Kartu {kartu.nama} berhasil ditambahkan ke deck.")
```

`isinstance(kartu, Kartu)` digunakan untuk memastikan object yang dimasukkan merupakan object dari class `Kartu`.

Jika valid, kartu dimasukkan ke dalam `daftar_kartu`.

## C. Menampilkan Deck

```python
def tampilkan_deck(self):
    if not self.daftar_kartu:
        print("Deck kosong.")
        return
    print("Daftar Kartu dalam Deck:")
    for idx, k in enumerate(self.daftar_kartu, 1):
        print(f"{idx}. {k.nama} - Tipe: {k.tipe}, Cost: {k.cost}, Dmg/Efek: {k.damage}")
```

Method ini mengecek apakah deck kosong.

Jika tidak kosong, program melakukan perulangan untuk menampilkan semua kartu yang ada di dalam deck.

---

# 4. Class Karakter

`Karakter` merupakan **superclass** yang menjadi dasar untuk class `Hero` dan `Musuh`.

## A. Constructor dan Encapsulation

```python
class Karakter:
    nama_game = "Roguelite Card Battle Simulator"

    def __init__(self, nama, health):
        # Protected attribute untuk nama dan darah karakter
        self._nama = nama
        self._health = health

        # Private attribute untuk id karakter
        self.__id_karakter = id(self)
```

`_nama` dan `_health` menggunakan **protected attribute**. Atribut ini dapat digunakan oleh subclass seperti `Hero` dan `Musuh`.

`__id_karakter` menggunakan **private attribute** karena hanya menjadi data internal dari `Karakter`.

## B. Method Status

```python
def status(self):
    print(f"Nama Karakter: {self._nama}")
    print(f"{self._nama} - Health: {self._health}")
```

Method `status()` menampilkan informasi dasar karakter.

Method ini nantinya **dioverride** oleh `Hero` dan `Musuh` agar masing-masing dapat menampilkan informasi yang lebih spesifik.

## C. Property Health

```python
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
```

Property `health` digunakan untuk mengakses dan mengubah `_health`.

Setter melakukan validasi agar health:

* Berupa angka.
* Tidak bernilai negatif.

---

# 5. Class Hero

`Hero` merupakan subclass dari `Karakter`.

## A. Inheritance dan Constructor

```python
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

        # KOMPOSISI: Hero membuat dan memiliki objek Deck internal secara langsung
        self.deck = Deck()
        Hero.total_hero += 1
```

`class Hero(Karakter)` menunjukkan bahwa `Hero` mewarisi `Karakter`.

`super().__init__(nama, health)` digunakan untuk memanggil constructor dari superclass.

Atribut khusus `Hero`:

* `class_hero` untuk menyimpan class dari hero.
* `__block` untuk menyimpan nilai pertahanan hero.
* `energy` untuk menyimpan energi saat ini.

`self.deck = Deck()` menunjukkan **composition**, karena object `Deck` dibuat langsung di dalam object `Hero`.

## B. Method Overriding

```python
def status(self):
    print(f"[Hero] {self._nama}")
    print(f"  Class       : {self.class_hero}")
    print(f"  Health      : {self._health}")
    print(f"  Block       : {self.__block}")
    print(f"  Total Kartu : {len(self.deck.daftar_kartu)}")
```

Method `status()` pada `Hero` menggantikan method `status()` dari `Karakter`.

Karena di-override, `Hero` dapat menampilkan informasi tambahan seperti:

* Class hero
* Health
* Block
* Jumlah kartu dalam deck

## C. Association dengan Kartu dan Musuh

```python
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
```

Method ini menunjukkan **association** karena `Hero` berinteraksi dengan object `Kartu` dan `Musuh`.

Kartu dicek terlebih dahulu apakah terdapat di dalam deck.

Jika energi cukup, cost kartu dikurangi dari energy hero dan damage kartu diberikan kepada target melalui `terima_damage()`.

## D. Property Block

```python
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
```

Property `block` digunakan untuk mengakses private attribute `__block`.

Setter memastikan nilai block berupa angka dan tidak negatif.

## E. Class Method dan Static Method

```python
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
```

`info_hero()` merupakan class method untuk menampilkan informasi yang dimiliki oleh class `Hero`.

`validasi_nama_hero()` merupakan static method untuk mengecek apakah nama hero berupa string dan tidak kosong.

---

# 6. Class Musuh

`Musuh` juga merupakan subclass dari `Karakter`.

## A. Inheritance dan Constructor

```python
class Musuh(Karakter):
    tingkat_kesulitan = "Normal"
    total_musuh = 0

    def __init__(self, nama, aksi_musuh, health, intent_damage):
        super().__init__(nama, health)
        self.aksi_musuh = aksi_musuh
        self.__intent_damage = intent_damage
        Musuh.total_musuh += 1
```

`Musuh(Karakter)` menunjukkan inheritance dari `Karakter`.

`super().__init__(nama, health)` memanggil constructor dari superclass.

Atribut khusus `Musuh`:

* `aksi_musuh` untuk menyimpan rencana aksi musuh.
* `__intent_damage` untuk menyimpan damage yang akan dilakukan musuh.

## B. Method Overriding

```python
def status(self):
    print(f"[Musuh] {self._nama}")
    print(f"  Rencana Aksi: {self.aksi_musuh}")
    print(f"  Health      : {self._health}")
    print(f"  Intent Dmg  : {self.intent_damage}")
```

Method `status()` meng-override method dari `Karakter`.

Versi `Musuh` menampilkan informasi yang sesuai dengan kebutuhan musuh, seperti rencana aksi dan intent damage.

## C. Method Menerima Damage

```python
def terima_damage(self, damage):
    if not isinstance(damage, (int, float)):
        print("  Status      : Damage harus berupa angka.")
        return
    if damage < 0:
        print("  Status      : Damage tidak boleh negatif.")
        return

    self._health -= damage

    if self._health < 0:
        self._health = 0

    print(f"{self._nama} menerima {damage} damage. Health sekarang: {self._health}")
```

Method ini digunakan ketika musuh menerima serangan.

Damage divalidasi terlebih dahulu. Setelah itu health dikurangi sesuai damage.

Jika health menjadi kurang dari `0`, nilainya diubah menjadi `0`.

## D. Property Intent Damage

```python
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
```

Property ini digunakan untuk mengakses private attribute `__intent_damage`.

Setter melakukan validasi agar intent damage berupa angka dan tidak negatif.

## E. Class Method dan Static Method

```python
@classmethod
def info_total_musuh(cls):
    print(f"Total Musuh Aktif   : {cls.total_musuh}")

@staticmethod
def validasi_damage(damage):
    if not isinstance(damage, (int, float)):
        return False
    return damage >= 0
```

`info_total_musuh()` digunakan untuk menampilkan jumlah object `Musuh` yang telah dibuat.

`validasi_damage()` merupakan static method untuk mengecek apakah nilai damage valid.

---

# 7. Relasi Antar Class

## A. Inheritance

```python
class Karakter:
    ...

class Hero(Karakter):
    ...

class Musuh(Karakter):
    ...
```

`Hero` dan `Musuh` merupakan subclass dari `Karakter`.

Relasinya:

```text
             Karakter
              /     \
             /       \
          Hero      Musuh
```

Keduanya mendapatkan atribut dan method dari `Karakter`, kemudian dapat menambahkan atribut serta method sendiri.

---

## B. Composition

Bagian yang menunjukkan composition terdapat pada constructor `Hero`:

```python
def __init__(self, nama, class_hero, health, block):
    super().__init__(nama, health)
    self.class_hero = class_hero
    self.__block = block
    self.energy = Hero.max_energy

    self.deck = Deck()
```

`Hero` membuat object `Deck` secara langsung melalui:

```python
self.deck = Deck()
```

Artinya `Deck` menjadi bagian dari object `Hero`.

Relasinya:

```text
Hero ◆──── Deck
```

`◆` menunjukkan **composition**.

---

## C. Aggregation

Pada class `Deck`, object `Kartu` hanya disimpan ke dalam list:

```python
class Deck:
    def __init__(self):
        self.daftar_kartu = []

    def tambah_kartu(self, kartu: Kartu):
        if isinstance(kartu, Kartu):
            self.daftar_kartu.append(kartu)
```

Object kartu dibuat secara terpisah:

```python
strike = Kartu("Strike", "Serangan", 1, 6)
defend = Kartu("Defend", "Pertahanan", 1, 5)
```

Kemudian kartu tersebut dimasukkan ke deck:

```python
deck_baru = Deck()
deck_baru.tambah_kartu(strike)
deck_baru.tambah_kartu(defend)
```

Karena `Kartu` sudah dibuat secara independen dan masih dapat digunakan di luar `Deck`, relasi ini merupakan **aggregation**.

Relasinya:

```text
Deck ◇──── Kartu
```

`◇` menunjukkan **aggregation**.

---

## D. Association

Association ditunjukkan melalui method:

```python
def gunakan_kartu(self, kartu: Kartu, target: 'Musuh'):
    if kartu in self.deck.daftar_kartu:
        if self.energy >= kartu.cost:
            self.energy -= kartu.cost
            target.terima_damage(kartu.damage)
            print(f"{self._nama} menggunakan {kartu.nama} pada {target._nama}.")
```

`Hero` menggunakan object `Kartu` untuk memberikan damage kepada object `Musuh`.

Jadi terdapat hubungan penggunaan antara:

```text
Hero ───── Kartu
  \
   \
    └──── Musuh
```

Relasi ini merupakan **association** karena ketiga object dapat tetap berdiri sendiri.

---

# 8. Pengujian Program

## A. Membuat Object

```python
strike = Kartu("Strike", "Serangan", 1, 6)
defend = Kartu("Defend", "Pertahanan", 1, 5)

ironclad = Hero("Ironclad", "Warrior", 80, 0)
silent = Hero("Silent", "Rogue", 70, 5)

cultist = Musuh("Cultist", "Menyerang", 50, 6)
jaw_worm = Musuh("Jaw Worm", "Menyerang/Bertahan", 40, 7)
```

Dibuat minimal dua object untuk setiap class yang digunakan dalam pengujian.

Object tersebut terdiri dari:

* 2 `Kartu`
* 2 `Hero`
* 2 `Musuh`

---

## B. Pengujian Inheritance

```python
print(f"Hero merupakan Karakter : {isinstance(ironclad, Karakter)}")
print(f"Musuh merupakan Karakter : {isinstance(cultist, Karakter)}")

print()

print("Hero memanggil method status() hasil overriding:")
ironclad.status()

print()

print("Musuh memanggil method status() hasil overriding:")
cultist.status()
```

`isinstance()` digunakan untuk membuktikan bahwa object `Hero` dan `Musuh` merupakan bagian dari `Karakter`.

Pemanggilan `status()` juga menunjukkan bahwa masing-masing subclass menggunakan method `status()` hasil overriding.

---

## C. Pengujian Association

```python
ironclad.deck.tambah_kartu(strike)
ironclad.deck.tambah_kartu(defend)

print()
ironclad.deck.tampilkan_deck()

print()
print(f"Health Cultist sebelum : {cultist.health}")
ironclad.gunakan_kartu(strike, cultist)
print(f"Health Cultist sesudah : {cultist.health}")
```

Pada pengujian ini:

1. `Strike` dan `Defend` dimasukkan ke deck `Ironclad`.
2. `Ironclad` menggunakan `Strike`.
3. `Strike` memberikan damage kepada `Cultist`.
4. Health `Cultist` berubah dari `50` menjadi `44`.

Hal ini menunjukkan interaksi antara `Hero`, `Kartu`, dan `Musuh`.

---

## D. Pengujian Aggregation

```python
deck_baru = Deck()
deck_baru.tambah_kartu(strike)
deck_baru.tambah_kartu(defend)

print()
deck_baru.tampilkan_deck()

print()
print("Kartu Strike tetap dapat digunakan di luar Deck:")
strike.info_kartu()
```

`Strike` dan `Defend` sebelumnya sudah dibuat sebagai object `Kartu`.

Object tersebut kemudian dimasukkan ke `deck_baru`.

`Strike` tetap dapat digunakan secara langsung setelah dimasukkan ke deck. Hal ini menunjukkan bahwa keberadaan kartu tidak bergantung pada `Deck`.

---

## E. Pengujian Composition

```python
print(f"Deck milik {ironclad._nama} dibuat otomatis: {isinstance(ironclad.deck, Deck)}")
print(f"Jumlah kartu dalam deck: {len(ironclad.deck.daftar_kartu)}")

print()
print("Deck merupakan bagian dari objek Hero.")
ironclad.deck.tampilkan_deck()
```

Object `Deck` sudah otomatis dibuat ketika object `Hero` dibuat.

Hasil `isinstance()` bernilai `True`, sehingga dapat dibuktikan bahwa `Hero` memiliki object `Deck` di dalamnya.

---

# 9. Hasil Program

```text
====================================================
      Simulasi Deck Building Berbasis Giliran
====================================================
  Status      : Health Ironclad berhasil diubah.
  Status      : Health Silent berhasil diubah.
  Status      : Health Cultist berhasil diubah.
  Status      : Health Jaw Worm berhasil diubah.

----------------------------------------------------
                  UJI INHERITANCE
----------------------------------------------------
Hero merupakan Karakter : True
Musuh merupakan Karakter : True

Hero memanggil method status() hasil overriding:
[Hero] Ironclad
  Class       : Warrior
  Health      : 80
  Block       : 0
  Total Kartu : 0

Musuh memanggil method status() hasil overriding:
[Musuh] Cultist
  Rencana Aksi: Menyerang
  Health      : 50
  Intent Dmg  : 6

----------------------------------------------------
               UJI RELASI ASSOCIATION
----------------------------------------------------
Kartu Strike berhasil ditambahkan ke deck.
Kartu Defend berhasil ditambahkan ke deck.

Daftar Kartu dalam Deck:
1. Strike - Tipe: Serangan, Cost: 1, Dmg/Efek: 6
2. Defend - Tipe: Pertahanan, Cost: 1, Dmg/Efek: 5

Health Cultist sebelum : 50
  Status      : Health Cultist berhasil diubah.
Cultist menerima 6 damage. Health sekarang: 44
Ironclad menggunakan Strike pada Cultist.
  Sisa Energi: 2
Health Cultist sesudah : 44

----------------------------------------------------
               UJI RELASI AGGREGATION
----------------------------------------------------
Kartu Strike berhasil ditambahkan ke deck.
Kartu Defend berhasil ditambahkan ke deck.

Daftar Kartu dalam Deck:
1. Strike - Tipe: Serangan, Cost: 1, Dmg/Efek: 6
2. Defend - Tipe: Pertahanan, Cost: 1, Dmg/Efek: 5

Kartu Strike tetap dapat digunakan di luar Deck:
Strike
  Tipe        : Serangan
  Energy Cost : 1
  Nilai Efek  : 6

----------------------------------------------------
               UJI RELASI COMPOSITION
----------------------------------------------------
Deck milik Ironclad dibuat otomatis: True
Jumlah kartu dalam deck: 2

Deck merupakan bagian dari objek Hero.
Daftar Kartu dalam Deck:
1. Strike - Tipe: Serangan, Cost: 1, Dmg/Efek: 6
2. Defend - Tipe: Pertahanan, Cost: 1, Dmg/Efek: 5
```

---

# 10. Kesimpulan

Program ini menerapkan beberapa konsep OOP melalui class `Kartu`, `Deck`, `Karakter`, `Hero`, dan `Musuh`.

Konsep yang diterapkan meliputi:

* **Encapsulation** melalui private dan protected attribute serta property.
* **Inheritance** melalui `Hero(Karakter)` dan `Musuh(Karakter)`.
* **Method overriding** melalui method `status()` pada `Hero` dan `Musuh`.
* **Association** melalui penggunaan `Kartu` dan `Musuh` oleh `Hero`.
* **Aggregation** melalui `Deck` yang menyimpan object `Kartu` yang dibuat secara independen.
* **Composition** melalui `Hero` yang membuat object `Deck` secara langsung.
* **Class method** dan **static method** untuk fungsi yang berkaitan dengan class maupun validasi.
