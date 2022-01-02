from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=500, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    in_stock = models.BooleanField(default=False, verbose_name='Есть в наличии')

    def __str__(self):
        return self.name + f"[{self.price}]"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name='Изображение')

    def __str__(self):
        return f"{self.item} {self.id}"

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товара'
