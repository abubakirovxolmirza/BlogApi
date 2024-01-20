# Blog App RESTful API Documentation
```bash
git clone https://github.com/abubakirovxolmirza/BlogApi
```
```bash
docker build -t blog:1.0 .
docker run -p 1212:8000 blog:1.0
```

## Blog Model

- `title` (string): Blog ning nomi.
- `content` (text): Blog ning tavsifi.
- `created_at` (datetime): Blog yaratilgan vaqti.
- `author` (string): Blog ni yaratgan foydalanuvchining usernamesi.

## HTTP so'rovlari va Javoblari

## Yangi blog post yaratish
![img1](blog/image/readme_img/new.png)
## Barcha blog postlar ro’yxatini ko’rsatish
![img2](blog/image/readme_img/blogs.png)
## {id} li blog postni yangilash
![img3](blog/image/readme_img/update.png)
## {id} li blog postni qaytarish
![img4](blog/image/readme_img/id.png)
## {id} li blog postni o’chirish
![img5](blog/image/readme_img/delete.png)
## {username} li odamni profilini ko’rsatish
![img6](blog/image/readme_img/user.png)

