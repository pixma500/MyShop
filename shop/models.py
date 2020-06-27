from django.db import models
from django.urls import reverse
from decimal import Decimal
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='категория' )
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class Tag (models.Model):
    title = models.CharField(max_length=70, db_index=True, verbose_name='теги')
    slug = models.SlugField(max_length=70, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_tag', args=[self.slug])




    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.PROTECT, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='products')
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название' )
    slug = models.SlugField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True, verbose_name='Изображение' )
    description = models.TextField(blank=True, verbose_name='Описание' )
    price = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='Цена' )
    available = models.BooleanField(default=True, verbose_name='Наличие' )
    created = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания' )
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления' )
    sale = models.DecimalField(max_digits=3, decimal_places=0, blank=True, default=0,verbose_name='Скидка в %')


    def get_price(self):
        return Decimal(self.price*(1 -self.sale/100)).quantize(Decimal('0.'))


    class Meta:
        ordering = ('-created','name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural ='Товары'

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name