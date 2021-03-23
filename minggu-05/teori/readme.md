### Input dan Output

Ada beberapa cara untuk mepresentasikan keluaran suatu program. Data dapat dicetak dalam bentuk yang dapat terbaca atau ditulis diberkas untuk digunakan dimasa mendatang.
Pilihan output :
* Dengan kurung kurawal sebagai index variabel. Contoh :
> print("Nama {0} NIM {1}").format('An Yunas','185410091')

* Dengan fungsi repr ( Repr hampir sama seperti string namun repr akan merepresentasikan nilai agar jika berubah dari tipe data maka akan muncul error ).
> print(repr("Hello world"))

Pilihan input :
* Membaca data , misal ada data bernama workfile
> f = open('workfile')

* Masukan Json
> import json
data = json.dumps([185410091, 'An Yunas'])

Metode pemasukkan data dan nilai dapat dengan baik dikelola dengan beberapa metode yang bisa digunakan sebagai alternatif yang lebih praktis maupun kompleks. Menampilkan suatu nilai juga dapat dilakukan dengan beberapa cara sesuai kebutuhan dalam kode dan praktik kali ini mempelajari beberapa hal itu.  