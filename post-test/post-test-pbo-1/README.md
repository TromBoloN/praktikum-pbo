# Sistem Simulasi Permainan Kartu Deck-Building Berbasis Giliran

## Deskripsi Program

Program ini merupakan implementasi dari **Sistem Simulasi Permainan Kartu Deck-Building Berbasis Giliran** menggunakan Python dan pendekatan PBO.

Konsep permainan mengambil inspirasi dari *Slay the Spire*, dengan tiga class utama:

* **Kartu** sebagai alat aksi yang digunakan dalam permainan.
* **Hero/Pemain** sebagai karakter yang dikendalikan pemain.
* **Musuh** sebagai lawan NPC dalam permainan.


## Struktur Class

```text
Sistem Permainan
│
├── Kartu
│   ├── Informasi kartu
│   ├── Cost
│   └── Damage
│
├── Hero/Pemain
│   ├── Informasi hero
│   ├── Health
│   └── Block
│
└── Musuh
    ├── Informasi musuh
    ├── Health
    └── Intent Damage
```

---

# 1. Class `Kartu`

Class `Kartu` digunakan untuk membuat dan mengelola data kartu.

### Class Attributes

| Atribut              | Tipe  | Keterangan                                 |
| -------------------- | ----- | ------------------------------------------ |
| `nama_game`          | `str` | Nama game.                                 |
| `total_kartu_dibuat` | `int` | Jumlah objek kartu yang telah dibuat.      |
| `kategori_game`      | `str` | Kategori permainan, yaitu `Deck-Building`. |

### Instance Attributes

| Atribut    | Tipe  | Keterangan                                           |
| ---------- | ----- | ---------------------------------------------------- |
| `nama`     | `str` | Nama kartu.                                          |
| `tipe`     | `str` | Jenis kartu.                                         |
| `__cost`   | `int` | Private attribute untuk menyimpan Energy Cost.       |
| `__damage` | `int` | Private attribute untuk menyimpan nilai damage/efek. |

### Method Utama

* `__init__()` — Menginisialisasi data objek dan menambah `total_kartu_dibuat`.
* `tampilkan_info_kartu()` — Menampilkan informasi kartu.
* `cost` — Getter dan setter untuk `__cost` dengan validasi nilai negatif dan tipe data.
* `damage` — Getter dan setter untuk `__damage` dengan validasi nilai negatif dan tipe data.
* `tampilkan_total_kartu()` — Class method untuk menampilkan jumlah kartu yang dibuat.
* `validasi_cost()` — Static method untuk memvalidasi nilai cost.

---

# 2. Class `Hero` / `Pemain`

Class ini digunakan untuk membuat dan mengelola data karakter yang digunakan pemain.

### Class Attributes

| Atribut        | Tipe  | Keterangan                                  |
| -------------- | ----- | ------------------------------------------- |
| `nama_game`    | `str` | Nama game.                                  |
| `max_energy`   | `int` | Maksimal Energy dalam satu giliran.         |
| `total_pemain` | `int` | Jumlah objek hero/pemain yang telah dibuat. |

### Instance Attributes

| Atribut      | Tipe  | Keterangan                           |
| ------------ | ----- | ------------------------------------ |
| `nama`       | `str` | Nama hero.                           |
| `class_hero` | `str` | Class atau tipe hero.                |
| `__health`   | `int` | Private attribute untuk Health.      |
| `__block`    | `int` | Private attribute untuk Block/armor. |

### Method Utama

* `__init__()` — Menginisialisasi data hero dan menambah `total_pemain`.
* `tampilkan_status()` / `status()` — Menampilkan status hero.
* `health` — Getter dan setter Health dengan validasi.
* `block` — Getter dan setter Block dengan validasi.
* `tampilkan_info_pemain()` / `info_hero()` — Class method untuk menampilkan informasi umum hero.
* `validasi_nama_hero()` — Static method untuk memvalidasi nama hero.

---

# 3. Class `Musuh`

Class `Musuh` digunakan untuk membuat dan mengatur data lawan NPC.

### Class Attributes

| Atribut             | Tipe  | Keterangan                            |
| ------------------- | ----- | ------------------------------------- |
| `nama_game`         | `str` | Nama game.                            |
| `tingkat_kesulitan` | `str` | Tingkat kesulitan permainan.          |
| `total_musuh`       | `int` | Jumlah objek musuh yang telah dibuat. |

### Instance Attributes

| Atribut           | Tipe  | Keterangan                                                |
| ----------------- | ----- | --------------------------------------------------------- |
| `nama`            | `str` | Nama musuh.                                               |
| `aksi_musuh`      | `str` | Rencana aksi musuh.                                       |
| `__health`        | `int` | Private attribute untuk Health musuh.                     |
| `__intent_damage` | `int` | Private attribute untuk damage yang akan diberikan musuh. |

### Method Utama

* `__init__()` — Menginisialisasi data musuh dan menambah `total_musuh`.
* `tampilkan_info_musuh()` / `info_musuh()` — Menampilkan informasi musuh.
* `health` — Getter dan setter Health dengan validasi.
* `intent_damage` — Getter dan setter Intent Damage dengan validasi.
* `tampilkan_total_musuh()` / `info_total_musuh()` — Class method untuk menampilkan jumlah musuh.
* `validasi_damage()` — Static method untuk memvalidasi nilai damage jika tersedia pada kode program.

---
## Penjelasan Output

1. **Class Method:**
   Program menampilkan informasi umum dari masing-masing class. `Kartu.total_kartu()` menampilkan jumlah kartu yang berhasil dibuat, yaitu 2 kartu. `Hero.info_hero()` menampilkan nama game, maksimal energi, dan jumlah hero yang dibuat, yaitu 2 hero. `Musuh.info_total_musuh()` menampilkan jumlah musuh yang dibuat, yaitu 2 musuh.

2. **Instance Method:**
   Program menampilkan informasi dari setiap objek yang telah dibuat. `Strike` dan `Defend` menampilkan tipe kartu, energy cost, dan nilai efek. `Ironclad` dan `Silent` menampilkan class, health, dan block. Sementara `Cultist` dan `Jaw Worm` menampilkan rencana aksi, health, dan intent damage masing-masing.

3. **Setter dan Validasi Data:**
   Program menguji perubahan nilai atribut menggunakan data valid dan tidak valid.

   * Health `Ironclad` berhasil diubah dari 80 menjadi 75 karena nilai yang diberikan valid.
   * Health `Silent` dicoba diubah menjadi `-10`, tetapi ditolak karena health tidak boleh bernilai negatif. Nilai health tetap 70.
   * Cost `Strike` dicoba diubah menjadi `-2`, tetapi ditolak karena cost tidak boleh negatif. Nilai cost tetap 1.
   * Cost `Defend` dicoba diubah menggunakan string `"dua"`, tetapi ditolak karena cost harus berupa angka. Nilai cost tetap 1.

4. **Static Method:**
   Program melakukan beberapa pengujian validasi tanpa membuat objek baru. Nama hero `"Ironclad"` menghasilkan `True` karena merupakan string yang tidak kosong, sedangkan angka `123` menghasilkan `False`. Validasi cost `-1` menghasilkan `False`, sedangkan cost `2` menghasilkan `True`. Cost `"dua"` juga menghasilkan `False` karena bukan angka. Pada validasi damage musuh, nilai `-5` menghasilkan `False`, nilai `10` menghasilkan `True`, dan string `"besar"` menghasilkan `False` karena bukan angka.

---

# Cara Menjalankan Program

Jalankan program dari folder `post-test/post-test-pbo-1`:

```bash
python main.py
```


