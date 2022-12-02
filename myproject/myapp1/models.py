from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название фильма')
    year = models.IntegerField(verbose_name='Год')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр')
    director = models.CharField(max_length=100, verbose_name='Режиссер')
    starring = models.TextField(verbose_name='В ролях')
    poster = models.ImageField(upload_to='posters/', verbose_name='Афиша фильма')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"{self.pk}. {self.title}. {self.year}"

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Genre(models.Model):
    genre = models.CharField(max_length=50, verbose_name='Жанр')

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'