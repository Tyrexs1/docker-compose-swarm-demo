# 🚀 Docker Secret, Compose, and Swarm – Secure Redis App

## 📌 Deskripsi
Proyek ini adalah latihan penggunaan **Docker Secret**, **Docker Compose**, dan **Docker Swarm** untuk mengelola aplikasi sederhana yang terhubung dengan Redis.  
Tujuan utama:
- Menyimpan password Redis secara aman menggunakan **Docker Secret**.
- Menjalankan aplikasi multi-container dengan **Docker Compose**.
- Mendeploy aplikasi di mode **Docker Swarm** untuk simulasi produksi.

---

## 🗂 Struktur Proyek
```bash
secure-web-app/
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
├── secrets/
│   └── redis_password.txt
├── Dockerfile
└── docker-compose.yml
```
---

## ⚙️ Cara Menjalankan

 1️⃣ Build Image
```bash
docker build -t hadiah_mbc1 .
```
2️⃣ Jalankan di Docker Compose
```bash
docker compose up
```
Akses aplikasi di browser: http://localhost:5000

3️⃣ Jalankan di Docker Swarm
Aktifkan Swarm:

```bash
docker swarm init
```
Buat secret :
```bash
docker secret create redis_password ./secrets/redis_password.txt
```
Deploy stack:
```bash
docker stack deploy -c docker-compose.yml week1_mbc
```
---

## 🔍 Pengujian Redis
Masuk ke container Redis:

```bash
docker exec -it <NAMA_CONTAINER_REDIS> sh
```
Masuk ke Redis CLI:
```bash
redis-cli -a password
```
Lihat pesan yang tersimpan:
```bash
LRANGE messages 0 -1
```
