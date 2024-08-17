from django.db import models
from django.urls import reverse

MAX_LENGTH = 255


class Supplier(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True, verbose_name='Название компании')
    agent_lastname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия представителя')
    agent_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя представителя')
    agent_surname = models.CharField(max_length=MAX_LENGTH, null=True, blank=True, verbose_name='Отчество представителя')
    phone = models.CharField(max_length=16, verbose_name='Телефон представителя')
    location = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес')
    is_exists = models.BooleanField(default=False, verbose_name='Логическое удаление')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("suppier_detail", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        

class Supply(models.Model):
    date_supply = models.DateTimeField(auto_now_add=True, verbose_name='Дата поставки')
    supplier = models.OneToOneField(Supplier, on_delete=models.CASCADE, verbose_name='Поставщик')
    
    product = models.ManyToManyField('Product', through='PosSupply', verbose_name='Товары')
    
    def __str__(self):
        return f'{self.date_supply} | {self.supplier.name}'
    
    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'


class Parametr(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Характеристика', unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
    

class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название', unique=True)
    description = models.CharField(max_length=MAX_LENGTH, null=True, blank=True, verbose_name='Описание')
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        

class Tag(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название', unique=True)
    description = models.CharField(max_length=MAX_LENGTH, null=True, blank=True, verbose_name='Описание')
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        
        
class Order(models.Model):
    SHOP = "SH"
    COURIER = "CR"
    PICKUPPOINT = "PP"
    TYPE_DELIVERY = [
        (SHOP, 'Магазин'),
        (COURIER, 'Доставка курьером'),
        (PICKUPPOINT, 'Пункт выдачи')
    ]
    buyer_lastname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия покупателя')
    buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя покупателя')
    buyer_surname = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Отчество покупателя')
    comment = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Комментарий к заказу')
    location = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Адрес доставки')
    delivery = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name='Способ доставки')
    create_data = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    end_data = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения')

    product = models.ManyToManyField('Product', through='PosOrder', verbose_name='Товар')
    
    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.pk} - ({self.buyer_lastname} {self.buyer_name}) {self.create_data}'
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Product(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True, verbose_name='Название')
    description = models.CharField(max_length=MAX_LENGTH, null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    photo = models.ImageField(upload_to='images/%Y/%m/%d', default='images/no_photo.png', null=True, blank=True, verbose_name='Картинка')
    is_exists = models.BooleanField(default=False, verbose_name='Логическое удаление')
    
    parament = models.ManyToManyField(Parametr, through='PosParametr', verbose_name='Характеристика', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True, verbose_name='Категория')
    tag = models.ManyToManyField(Tag, blank=True, null=True, verbose_name='Теги')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("one_product", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', '-price']
        
        
class PosParametr(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар')
    parametr = models.ForeignKey(Parametr, on_delete=models.PROTECT, verbose_name='Характеристика')
    value = models.CharField(max_length=MAX_LENGTH, verbose_name='Значение')
    
    def __str__(self):
        return f'{self.product.name} | {self.value}'
    
    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристики товаров'
        

class PosSupply(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE, verbose_name='Поставка')
    count = models.PositiveIntegerField(verbose_name='Кол-во товара')
    
    def __str__(self):
        return f'{self.supply.date_supply} | {self.product.name} ({self.count})'
    
    
    def get_absolute_url(self):
        return reverse("detail_supply", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name = 'Позиция поставки'
        verbose_name_plural = 'Позиции поставок'
        

class PosOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    count = models.PositiveIntegerField(verbose_name='Количество', default=1)
    discount = models.PositiveIntegerField(verbose_name='Скидка', default=0)
    
    def __str__(self):
        return f'{self.count} | {self.product.name} ({self.count})'
    
    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'
