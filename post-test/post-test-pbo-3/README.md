# POSTTEST 3 PBO 2026

Nama: Arif Abdurrahman Siddiq
NIM: 2509106064
Kelas: B1'25

## 1. Deskripsi Program

Program ini adalah simulasi sederhana deck-building card battle berbasis giliran (terinspirasi Slay the Spire). Pada posttest ini program dikembangkan dengan Abstraksi dan Polimorfisme, selain konsep OOP dari posttest sebelumnya (encapsulation, inheritance, association, aggregation, composition).

Class yang digunakan:

* `Kartu` (abstract class) dengan subclass `KartuAttack`, `KartuDefend`, `KartuSpesial`
* `Deck`
* `Karakter` dengan subclass `Hero` dan `Musuh`
* `Relic` dan `Potion` (tidak berhubungan lewat pewarisan, dipakai untuk duck typing)

---

## 2. Class Diagram

![Class Diagram](relasi-uml.png)

### Penjelasan Relasi

**Asosiasi (`Hero` → `Kartu`)**
`Hero` memakai `Kartu` lewat method `gunakan_kartu()`, lalu kartu dimainkan dengan `kartu.mainkan(self, target)`. `Hero` hanya menggunakan kartu saat bertarung dan tidak mengatur siklus hidupnya, sehingga relasinya asosiasi.

**Agregasi (`Deck` ◇→ `Kartu`)**
`Deck` menyimpan objek `Kartu` di list `daftar_kartu`, tetapi kartu dibuat di luar `Deck` (misalnya `strike = KartuAttack(...)`) lalu dimasukkan lewat `tambah_kartu()`. Kartu tetap ada dan dapat dipakai walaupun tidak berada di deck, sehingga `Kartu` bisa hidup sendiri. Itulah alasan relasinya agregasi.

**Komposisi (`Hero` ◆→ `Deck`)**
`Deck` dibuat langsung di dalam `Hero.__init__` lewat `self.deck = Deck()`. Deck milik hero tidak dibuat dari luar dan tidak bermakna tanpa hero pemiliknya, sehingga relasinya komposisi.

**Perbedaan agregasi vs komposisi:** pada agregasi, bagian (`Kartu`) dibuat independen dan bisa hidup tanpa pemegangnya (`Deck`). Pada komposisi, bagian (`Deck`) dibuat oleh pemiliknya (`Hero`) dan ikut hilang bersamanya.

**Pewarisan:** `KartuAttack`, `KartuDefend`, dan `KartuSpesial` mewarisi `Kartu`. `Hero` dan `Musuh` mewarisi `Karakter`. `Relic` dan `Potion` sengaja tidak punya induk.

---

## 3. Abstraksi

### Abstract Class `Kartu`

`Kartu` mewarisi `ABC` dan memiliki dua abstract method:

```python
class Kartu(ABC):
    @abstractmethod
    def efek(self, pemilik, target): ...

    @abstractmethod
    def deskripsi(self): ...
```

* `efek(pemilik, target)`: apa yang terjadi saat kartu dimainkan.
* `deskripsi()`: teks penjelasan efek kartu.

### Method Konkret `mainkan()`

Method ini dipakai bersama oleh semua subclass. Alurnya tetap (cek energi, kurangi energi), lalu efek yang berbeda-beda diserahkan ke subclass lewat `self.efek(...)`.

```python
def mainkan(self, pemilik, target):
    if pemilik.energy < self.cost:
        print(f"Energi tidak mencukupi untuk {self.nama}.")
        return
    pemilik.energy -= self.cost
    self.efek(pemilik, target)
```

### Subclass yang Mengimplementasikan Abstract Method

| Subclass | `efek()` | Atribut unik |
|---|---|---|
| `KartuAttack` | memberi damage ke target (`target.terima_damage`) | - |
| `KartuDefend` | menambah block pemilik | - |
| `KartuSpesial` | pemilik kehilangan HP, mendapat energi | `biaya_hp` |

Setiap subclass memanggil `super().__init__(...)` untuk mengisi atribut dari `Kartu`.

### Atribut Protected dan Private

* `__cost` (private) di `Kartu`, diakses lewat property `cost`.
* `_nilai` (protected) di `Kartu`, dipakai langsung oleh subclass.
* `_nama` dan `_health` (protected) di `Karakter`, `__block` (private) di `Hero`.
* `__jumlah_heal` (private) di `Potion`, `_bonus_energi` (protected) di `Relic`.

### Bukti Abstract Class Tidak Dapat Diinstansiasi

```python
try:
    k = Kartu("X", "Tes", 1, 1)
except TypeError as e:
    print("Kartu tidak bisa diinstansiasi:", e)
```

---

## 4. Polimorfisme

### A. Polimorfisme via Pewarisan

Method `efek()` dan `deskripsi()` di-override oleh `KartuAttack`, `KartuDefend`, dan `KartuSpesial` dengan perilaku berbeda. Semuanya dipanggil lewat satu loop yang berisi objek dari subclass berbeda, tanpa `if/elif`:

```python
for kartu in ironclad.deck.daftar_kartu:
    kartu.mainkan(ironclad, cultist)
```

Hasilnya: `Strike` memberi damage, `Defend` menambah block, `Bloodletting` menukar HP dengan energi.

Selain itu, `Hero` dan `Musuh` sama-sama memiliki `status()` (override dari `Karakter`) dan `terima_damage()` dengan perilaku berbeda. `Hero` menyerap damage dengan block terlebih dahulu, sedangkan `Musuh` langsung mengurangi health.

### B. Duck Typing

`Relic` dan `Potion` tidak berhubungan lewat pewarisan, tetapi keduanya punya method `gunakan(pemilik)`. Fungsi `pakai_item()` memanggil keduanya dengan cara yang sama, tanpa mengecek tipe:

```python
def pakai_item(item, pemilik):
    item.gunakan(pemilik)

for item in (lantern, health_potion):
    pakai_item(item, ironclad)
```

### C. Operator Overloading

Pada class `Kartu`:

* `__str__`: mengubah tampilan objek saat di-`print`, misalnya `Strike (Serangan, cost 1)`.
* `__lt__`: membandingkan kartu berdasarkan cost, sehingga `sorted()` dapat mengurutkan deck.

```python
def __str__(self):
    return f"{self.nama} ({self.tipe}, cost {self.cost})"

def __lt__(self, other):
    return self.cost < other.cost
```

### D. Tanpa Anti-Pattern

Program tidak memakai rantai `if/elif` yang mengecek `type()` atau string jenis untuk membedakan perilaku. Setiap objek menentukan perilakunya sendiri lewat method. (`isinstance` di `Deck.tambah_kartu` hanya untuk validasi input.)

---

## 5. Nilai Plus: Prinsip SOLID

* **OCP (Open/Closed Principle):** kartu baru dapat ditambahkan cukup dengan membuat subclass `Kartu` baru yang mengimplementasikan `efek()` dan `deskripsi()`, tanpa mengubah `Hero`, `Deck`, maupun `mainkan()`.
* **DIP (Dependency Inversion Principle):** `Hero.gunakan_kartu()` dan `Deck` bergantung pada abstraksi `Kartu` (cukup memanggil `mainkan()`), bukan pada kartu konkret tertentu seperti `KartuAttack`.

---

## 6. Hasil Program

> Ganti blok ini dengan screenshot terminal dari program kamu.

```text
====================================================
      Simulasi Deck Building Berbasis Giliran       
====================================================

----------------------------------------------------
                  BUKTI ABSTRAKSI
----------------------------------------------------
Kartu tidak bisa diinstansiasi: Can't instantiate abstract class Kartu without an implementation for abstract methods 'deskripsi', 'efek'

----------------------------------------------------
     POLIMORFISME: SATU LOOP, TIGA JENIS KARTU
----------------------------------------------------
Kartu Strike berhasil ditambahkan ke deck.
Kartu Defend berhasil ditambahkan ke deck.
Kartu Bloodletting berhasil ditambahkan ke deck.

Cultist menerima 6 damage. Health sekarang: 44
  Status      : Block berhasil diubah.
Ironclad mendapat 5 block. Total block: 5
  Status      : Health Ironclad berhasil diubah.
Ironclad kehilangan 3 HP dan mendapat 2 energi.
  Sisa HP: 77 | Energi: 3

Strike (Serangan, cost 1)

Deck diurutkan berdasarkan cost:
  Bloodletting (Spesial, cost 0)
  Strike (Serangan, cost 1)
  Defend (Pertahanan, cost 1)

----------------------------------------------------
              DUCK TYPING: RELIC DAN POTION
----------------------------------------------------
Relic Lantern aktif: Ironclad mendapat 1 energi. Energi: 4
  Status      : Health Ironclad berhasil diubah.
Potion Health Potion diminum: Ironclad pulih 10 HP. HP: 87
```

---

## 7. Kesimpulan

Program ini menerapkan:

* **Abstraksi** lewat abstract class `Kartu` (`efek()`, `deskripsi()`) dan method konkret `mainkan()`.
* **Polimorfisme via pewarisan** lewat override `efek()` pada `KartuAttack`, `KartuDefend`, `KartuSpesial`.
* **Duck typing** lewat `Relic` dan `Potion` yang dipanggil oleh `pakai_item()`.
* **Operator overloading** lewat `__str__` dan `__lt__` pada `Kartu`.
* **Asosiasi, agregasi, komposisi** antara `Hero`, `Deck`, `Kartu`.
* **SOLID (OCP dan DIP)** lewat desain `Kartu` sebagai abstraksi yang dipakai `Hero` dan `Deck`.