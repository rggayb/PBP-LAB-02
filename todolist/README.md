# Link menuju home page dan todolist
[Home page](https://lab02pbp.herokuapp.com/)

[Todolist page](https://lab02pbp.herokuapp.com/todolist/)

# Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF adalah singkatan dari Cross-site request forgeries. Hal ini semacam action yang berbahaya, yaitu action yang tidak terverif akan diambil atas nama pengguna yang telah diautentikasi. Lalu, disinilah csrf_token berfungsi yaitu untuk menggagalkan serangan scrf dengan membandingkan token yang dimasukkan oleh pengguna dengan yang disimpan di sesi pengguna. Contohnya jika ada suatu rute pengguna atau email  menerima suatu permintaan POST untuk mengubah alamat email pengguna yang diautentikasi. Rute ini akan mengantisipasi bahwa alamat email yang diinginkan pengguna akan dimasukkan dalam formulir input email. Pada django, tanpa adanya {% csrf token %} request post tidak akan diproses.

# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Tentu saja bisa. Akan tetapi, akan terlihat lebih berantakan. Secara gambar besar, hal pertama yang harus dilakukan adalah dengan membuat sebuah HTML yang berfungsi untuk menjadi kontainer page items kita. Lalu membuat items untuk ditampilkan dan juga tambahkan proses dan branch.

#  Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Setelah submisi, create_task() akan dijalankan untuk mendapatkan title dan description menggunakan salah satu HTTP request yaitu POST, khususnya dengan fungsi request.POST.get(). Hal ini akan membuat sebuah object baru di model yang sebelumnya sudah dibuat menggunakan data yang sudah disubmit. Kemudian, akan reverse dan menjalankan show_todo_list kembali ke main page dan menampillkan semua to-do list.

# Implementasi
1. Membuat app todolist dengan menggunakan perintah python manage.py startapp todolist
Add todolist URL path by appending todolist in the project_django/settings.py and add path('todolist/', include('todolist.urls')) in project_django/urls.py
2. Untuk path, pertama akses ke project_django/settings.py lalu tambahkan todolist. Kemudian, tambahkan path path('todolist/', include('todolist.urls')) di project_django/urls.py

3. Lalu, buat model di todolist/models.py dan tambahkan variable2 seperti user, date, title, description, dan is_finished.
4. Untuk tombol login, logout, dan register dibuat di views.py dan juga routingnya di urls.py

5. Untuk membuat todolist di mainpage, maka harus membuat show_todol_ist di views.py dan juga todolist.html

6. Tambahkan url pattern di urls.py

7. Kemudian deploy di HEROKU dengan pull, add, commit, and push ke GitHub