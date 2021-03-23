### Modul
    Modul adalah file yang berisi definisi dan pernyataan Python. Nama berkas adalah nama modul dengan akhiran .py diakhirnya. Dalam sebuah modul, nama modul (sebagai string) tersedia sebagai nilai variabel global __name__.

>>> Untuk mengimpor seluruh fungsi gunakan ( * )
>>> Jika nama modul diikuti oleh as, maka nama setelah as terikat langsung ke modul yang diimpor.


### Paket
    Paket adalah cara penataan namespace modul Python dengan menggunakan "dotted module names". Sebagai contoh, nama modul A.B menetapkan submodule bernama B dalam sebuah paket bernama A. Berikut adalah struktur yang mungkin untuk paket Anda (dinyatakan dalam hierarki sistem file):
``` 
SOUND/                          TOP-LEVEL PACKAGE
      __INIT__.PY               INITIALIZE THE SOUND PACKAGE
      FORMATS/                  SUBPACKAGE FOR FILE FORMAT CONVERSIONS
              __INIT__.PY
              WAVREAD.PY
              WAVWRITE.PY
              AIFFREAD.PY
              AIFFWRITE.PY
              AUREAD.PY
              AUWRITE.PY
              ...
      EFFECTS/                  SUBPACKAGE FOR SOUND EFFECTS
              __INIT__.PY
              ECHO.PY
              SURROUND.PY
              REVERSE.PY
              ...
      FILTERS/                  SUBPACKAGE FOR FILTERS
              __INIT__.PY
              EQUALIZER.PY
              VOCODER.PY
              KARAOKE.PY
              ...

```