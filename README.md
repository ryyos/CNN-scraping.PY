<h1 align="center" >Hello 👋, I'm Ryo</h1>
<h3 align="center" >An independent backend developer</h3>

<h1 align="center" >Welcome To CNN-Scraping.PY🧣</h1>

> Program ini digunakan untuk mengambil data dari website berita CNN

## Feature

- penggunaan requests daripada webdriver (selenium/playwright) sehingga dapat berjalan lebih cepat dan ringan
- penggunaan Pyquery dari pada BS4 (Beautiful soup) sehingga lebih mudah untuk memparser (filter) content HTML untuk mengambil data yang di butuhkan
- penggunaan logging untuk mempermudah dalam memonitoring data
- mengambil data mulai dari berita yang paling update
- dapat mengambil 1000 page berita dalam 1 kali run

## Tech

- [icecream](https://github.com/gruns/icecream) adalah library Python yang menyediakan cara sederhana dan informatif untuk mencatat kode, membantu memantau alur eksekusi program.
- [requests](https://requests.readthedocs.io/) adalah library Python yang mudah digunakan untuk berinteraksi dengan API dan membuat permintaan HTTP.

## Requirement

- [Python](https://www.python.org/) v3.11.6+
- [icecream](https://github.com/gruns/icecream) v2.1.3+
- [requests](https://requests.readthedocs.io/) v2.31.0+

## Installation

> Untuk menjalankan program ini Anda perlu menginstal beberapa librarys dengan perintah

```sh
pip install -r requirements.txt
```

## How To Run ?🤔

```bash
# Clone this repositories
git clone https://github.com/ryosoraa/CNN-scraping.PY.git

# go into the directory
cd CNN-scraping.PY

```

Untuk menjalankan Programnya kamu hanya perlu menjalankan dengan command

```bash
python main.py
```

## 🚀Structure

```
│   LICENSE
│   main.py
│   README.md
│   requirements.txt
│
├───data
└───libs
    │   __init__.py
    │
    ├───service
    │       cnn.py
    │
    └───utils
            corrector.py
            logs.py
            parser.py
            writer.py
```

## Author

👤 **Rio Dwi Saputra**

- Twitter: [@ryosora12](https://twitter.com/ryosora12)
- Github: [@ryosoraa](https://github.com/ryosoraa)
- LinkedIn: [@rio-dwi-saputra-23560b287](https://www.linkedin.com/in/rio-dwi-saputra-23560b287/)
- Instagram: [@ryosoraa](https://www.instagram.com/ryosoraaa/)

<a href="https://www.linkedin.com/in/ryosora/">
  <img align="left" alt="Ryo's LinkedIn" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a href="https://www.instagram.com/ryosoraaa/">
  <img align="left" alt="Ryo's Instagram" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" /> 
</a>
