# Link menuju home page dan todolist
[Home page](https://lab02pbp.herokuapp.com/)

[Todolist page](https://lab02pbp.herokuapp.com/todolist/)

# Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

1. Inline CSS : Penggunaannya adalah dengan atribut <style> pada tag HTML tertentu. Ada kekurangan dan kelebihan dalam memakai style ini. Kelebihanya adalah ketika kita ingin memberi CSS hanya kepada satu tag saja. Karena, penggunaan style ini akan mengoverride seluruh CSS yang ada dan itu bisa menjadi kekurangan jika dilakukan di momen yang tidak tepat. Akan lebih sulit untuk di handle.

2. Internal CSS : Sesuai namanya, internal CSS akan bekerja pada satu halaman saja. Implementasinya ada pada head dalam suatu page HTML dengan tag <style>. Karena bekerja pada satu halaman, jadi setiap pindah page CSS harus load ulang.

3. External CSS : Sesuai namanya, external CSS adalah suatu style dengan membuat file css yang berbeda dengan HTMLL. File CSS tersebut nantinya akan di link dengan file HTML dengan memanggil referensi file cssnya. Salah satu keuntungan menggunakan style ini adalah dari efisiensi halaman. Jika kita punya sebuah website yang setiap halamannya menggunakan CSS yang mirip, menggunakan external CSS merupakan salah satu pilihan yang tepat. Karena kita tidak perlu ubah setiap halamannya, jika ada sedikit bagian yang ingin diubah bisa menggunakan inline css.

# Jelaskan tag HTML5 yang kamu ketahui.
tag pada HTML5 yang saya ketahui adalah :
<h1>, <h2>, ... <h-i> : tag untuk header sampe ke-i untuk berbagai macam ukuran.
<p> : tag untuk text
<style> : tag untuk mendefinisikan internal CSS dalam suatu halaman HTML
<a> : tag hyperlink
<button> : tag untuk sebuah tombol
<div> : tag untuk mendefinisikan suatu divisi atau bisa dianggap seperti kontainer
dan masih banyak lagi

#  Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Setelah submisi, create_task() akan dijalankan untuk mendapatkan title dan description menggunakan salah satu HTTP request yaitu POST, khususnya dengan fungsi request.POST.get(). Hal ini akan membuat sebuah object baru di model yang sebelumnya sudah dibuat menggunakan data yang sudah disubmit. Kemudian, akan reverse dan menjalankan show_todo_list kembali ke main page dan menampillkan semua to-do list.

# Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Class Selector : Memakai class yang sudah terdefinisi pada tag sebagai selectornya. Cara mengimplementasinya adalah dengan memakai nama classnya lalu didahului oleh . di depan selector tersebut. Saya mengimplementasinya pada saat membuat style dan menggunakan .card untuk selectornya

ID Selector : Mirip dengan class selector, tetapi Selector ini langsung menggunakan ID yang sudah didefinisikan pada tag sebagai selector-nya. Cara implementasinya adalah dengan menggunakan id pada tag tersebut, dan diberi # di depan selectornya.

# Implementasi Checklist
1. Memasukkan link <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous"> pada head di file base.html pada project django dan juga <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script> pada body

2. Modifikasi login.html dengan menggunakan external CSS style. Saya membuat file login.css yang terpisah lalu saya link dengan login.html dengan style yang sudah dibuat.

3. Modifikasi register.html dengan layout dan components yang saya sudah sesuaikan agar responsive juga

4. Modifikasi todolist.html. Pada todolist ini, saya mengimplementasi card dengan memanggil class card dan memasukkannya pada kontainer. Lalu card ini saya style juga dengan menggunakan internal CSS. Saya juga mengimplementasi hover disini sebagai bonus. Ketika cursor mengarah pada card, maka gradasi akan berpindah pada text dan juga border menghilang.

5. Modifikasi create_task.html memakai cara yang sama dengan login.html

6. melakukan add, commit, push ke GitHub dan selesai.