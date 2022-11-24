# Link menuju home page dan todolist
[Home page](https://lab02pbp.herokuapp.com/)

[Todolist page](https://lab02pbp.herokuapp.com/todolist/)

#  Jelaskan perbedaan antara asynchronous programming dengan synchronous programming!
Synchronous programming akan menjalankan program secara sequential, saat sedang mengeksekusi program akan terjadi antrian sehingga kita tidak bisa melakukan perintah lain sampai proses selesai di eksekusi. Asynchronous programming bisa menjalankan proses program secara bersamaan tanpa harus menunggu proses antrian

# Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming, sesuai namanya, akan ada sebuah "event" yang terjadi ketika user melakukan sebuah action. Contohnya seperti click button di halaman. Ketika user melakukan action tersebut maka program akan melakukan tugas lain. Pada tugas ini penerapannya adalah ketika tombol new task di click maka akan muncul modal.

# Jelaskan penerapan asynchronous programming pada AJAX.
Penerapannya untuk melakukan permintaan data dan menangani tanggapan baik response dalam bentuk JSON atau XML dari sebuah API.

# Implementasi Checklist
1. Menambahkan function show_json untuk menampilkan data pada website dalam bentuk json di views.py

2. Menambahkan function add_task_ajax untuk menambahkan data - data pada modal secara Asynchronous pada views.json

3. menambahkan path json/ dan add/ pada file urls.py

4. menambahkan link bootstrap CSS dan JS pada file HTMl agar bisa menggunakan AJAX dan tools bootstrap

5. menambahkan function refreshTodoList untuk reset isi halaman dan menampilkan tampilan baru

6. menambahkan function getTodolist untuk mendapatkan data data json

7. menambahkan function addTodoList untuk menambahkan todolist baru

8. menambahkan function updateTask dan deleteTask untuk update status dan delete card

6. melakukan add, commit, push ke GitHub dan selesai.