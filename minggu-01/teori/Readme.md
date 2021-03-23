## Kenapa Python?
- [x] Python memungkinkan keringanan terhadap program mempercepat proses dengan mengandalkan hal ini python menjadi bahasa dengan tingkat ke praktis'an yang tinggi.
- [x] Mudah digunakan tanpa menghilangkan kekompleks'an suatu bahasa pemrograman.
- [x] Dapat memisahkan program anda menjadi modul yang dapat digunakan kembali dan python dilengkapi modul yang luas dan sangat bervariasi.
- [x] Tipe data kompleks, Grouping kode, minim deklarasi.

## Interpreter python
Setelah mengunduh python terdapat interpreter yg dapat digunakan. Interpreter terdapat di path instalasi python atau anda dapat mencarinya. Interpreter ini mirip seperti cmd atau shell os linux dan dapat mengeksekusi file script python dengan menuliskan path lokasi filenya.
Tiap argumen akan menjadi sebuah list of string dan dapat dilihat dengan mengimport modul sys.
Interface yang didapat adalah tiga tanda lebih besar dari ( >>> ) untuk line pertama (primary) dan untuk kode yg membutuhkan line secondary akan ditandai dengan tiga tanda titik (...).
> \>\>\> Kode anda disini :
> ...   Kode terusan anda
> ...

#### Encoding
Secara default file python menggunakan encoded UTF-8 pada encoding ini karakter dari kebanyakan bahasa dapat di gunakan pada string, literal ,indentifier dan komen.
Encoding dapat diubah dengan kode
> -*- coding: encoding -*-

## Menggunakan Python
#### Sebagai kalkulator
Python bisa melakukan operasi matematika dengan symbol operator aritmatika seperti pada tabel.
 Symbol | Operator
 ------ | -------
 \+     | Penjumlahan
 \-     | Pengurangan
 \*     | Perkalian
 /      | Pembagian
 %      | Modulus(sisa bagi)
 ( )    | Prioritas
 **     | Pangkat
 //     | Pembagian (integer)

#### Menggunakan string
Python bisa memanipulasi string dengan mendeklarasikannya menggunakan petik satu('') maupun petik dua("").
Jika langsung di eksekusi maka output pada interpreter akan menunjukkan tanda petiknya juga. Untuk menghindari ini gunakan perintah _print_.
> print("String anda")
Tambahkan \n untuk baris baru string (tambahkan r didepan petik untuk string yang terdapat simbol \n itu didalamnya). Gunakan 3 tanda petik untuk string yg menggunakan line secondary(banyaknya lebih dari sebaris).
Bagian string dapat diakses melalui index dengan kode namastring[index]. Bagian string tidak dapat diubah hanya dapat dilihat dan disusun.
Menghitung banyaknya karakter pada sting dengan _len(String)_.

#### List
List bisa menampung item dari banyak tipe data tapi lebih sering digunakan untuk hanya satu tipe. contoh membuat list :
> squares = [1, 4, 9, 16, 25]
Data list dapat diakses dan diubah sesuka hati dengan index nya.
Menambahkan dibelakang list dengan _namaList.append(NILAI)_.

List dapat berisi banyak list didalamnya. contoh :

'''

>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'

'''

