from django.db import models

# Create your models here.
class menu_item(models.Model):
    #текст метки - verbose_name
    title = models.CharField(max_length=70, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Цена')

    TYPE = {
        ('CHI', 'Куриные'),
        ('BEF', 'Говяжьи'),
        ('VEG', 'Веганские')
    }
    type=models.CharField(choices=TYPE,max_length=3,default='NEW',verbose_name='Тип')

    def __str__(self):
        return self.title
