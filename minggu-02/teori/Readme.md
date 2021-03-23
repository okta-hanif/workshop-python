## Control Flow

1. ### If else
Di python if else tidak butuh tanda kurung untuk kondisi () dan statement dimulai setelah tanda titik dua ' : '.
> if _kondisi_ : 
>    _Statement_ 
    
note : else if ditulis menjadi ' elif '

2. ### For loop
For sangat berbeda dengan bahasa lain karna di python lebih mudah untuk mengolah list. For menggunakan in pada python, contoh :
```
words = ['cat', 'window', 'defenestrate']
for w in words: 
    print (w, len(w))
```

* range() dalam for
> for i in range(5)

melakukan print 1 - 4, note: nilai dalam range tidak include. 
bisa dikombinasikan dengan list untuk range index yg diinginkan.

* break, continue, dan else didalam loop
    * Gunakan break untuk mengakhiri loop jika kondisi terpenuhi.
    * Gunakan continue saat kondisi terpenuhi maka kode anda akan dilangkahi.
    * Gunakan else didalam loop (bukan setelah if) maka statement nya akan dijalankan bila for loop tidak terpenuhi.

3. ### Pernyataan pass
Hanya satu yg dilakukan oleh perintah pass yaitu :
- [x] Tidak melakukan apa-apa
Biasanya dibuat untuk kerangka fungsi/class 

4. ### Mendefinisikan Fungsi
Gunakan perintah :
> def nama_fungsi(parameter) :
>   _Statement_

Note : 
* Fungsi yang tidak mengembalikan nilai biasa disebut prosedur
* return pada fungsi mengembalikan nilai default _none_

## Lebih lanjut soal pendefinisian fungsi
1. ### Argumen bawaan
Pada suatu fungsi kita bisa mendefinisikan nilai atribut default.
contoh : 
> def ask_ok(prompt, retries=4, reminder='Please try again!'):

nilai atribut retries dan reminder sudah di set seperti diatas, jadi walau pengguna tidak memasukkan nilai atribut maka atribut punya nilai default.

Note : nilai default akan di update ke nilai berikutnya jika setingan nilai sudah di setting

2. ### Argumen Keyword 
Adalah argumen yang harus ada pada deklarasi fungsi , sbg contoh
> def parrot(voltage, state='a stiff', action='voom'

disana voltage adalah keyword karna jika tidak di beri nilai saat Fungsi dipanggil maka akan error.

tambahkan bintang di depan keyword untuk menandakan butuh nilai berapa, 1 dimulai dari 0 bintang , contoh yang butuh nilai 3:
> **keyword

3. ### Parameter spesial
Parameter bisa diatur seperti dibawah ini
```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

## Dokumentasi String
Jika ada lebih banyak baris dalam string dokumentasi, baris kedua harus kosong, memisahkan ringkasan secara visual dari sisa deskripsi.
Berikut contoh multi baris :
```
def my_function():
    """Do nothing, but document it.

         No, really, it doesn't do anything.
       """
     pass
```
