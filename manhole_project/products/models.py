from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class ProductImage(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    image = models.ImageField("Изображение", upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"

    def __str__(self):
        return f"Изображение для {self.content_object.name if self.content_object else 'неизвестного товара'}"


class Product(models.Model):
    name = models.CharField("Название", max_length=200)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to='products/', null=True, blank=True)
    specifications = models.TextField("Характеристики", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
         
    def get_specifications(self):
        specs = []
        
        # Добавляем общие характеристики
        if self.specifications:
            specs.append(self.specifications)
        
        # Получаем все поля модели (включая дочерние)
        for field in self._meta.get_fields():
            # Пропускаем служебные поля и поля базового класса
            if field.name in ['id', 'product_ptr', 'created_at', 'name', 'description', 'image', 'specifications']:
                continue
                
            # Получаем значение поля
            value = getattr(self, field.name, None)
            
            # Пропускаем пустые значения
            if not value:
                continue
                
            # Получаем человекочитаемое название поля
            verbose_name = getattr(field, 'verbose_name', field.name)
            
            # Для полей с choices показываем значение, а не ключ
            if hasattr(field, 'choices') and field.choices:
                value = dict(field.choices).get(value, value)
            
            specs.append(f"{verbose_name}: {value}")
        
        return specs


# --- Люк ---
class Lyuk(Product):
    TIP_VES_CHOICES = [
        ('Легкий', 'Легкий'),
        ('Средний', 'Средний'),
        ('Тяжелый', 'Тяжелый'),
    ]

    naruzhnyy_razmer = models.CharField("Наружный размер", max_length=100, blank=True)
    vysota = models.CharField("Высота", max_length=100, blank=True)
    vnutrenniy_diametr = models.CharField("Внутренний диаметр", max_length=100, blank=True)
    glubina_ustanovki_kryshki = models.CharField("Глубина установки крышки", max_length=100, blank=True)
    nominalnaya_nagruzka = models.CharField("Номинальная нагрузка", max_length=100, blank=True)
    ves = models.CharField("Вес", max_length=100, blank=True)
    tip_vesa = models.CharField("Тип по весу", max_length=50, choices=TIP_VES_CHOICES)

    class Meta:
        verbose_name = "Люк"
        verbose_name_plural = "Люки"


# --- Дождеприемник ---
class Dozhdiepriemnik(Product):
    naruzhnyy_razmer = models.CharField("Наружный размер", max_length=100, blank=True)
    vysota = models.CharField("Высота", max_length=100, blank=True)
    vnutrenniy_diametr = models.CharField("Внутренний диаметр", max_length=100, blank=True)
    glubina_ustanovki_kryshki = models.CharField("Глубина установки крышки", max_length=100, blank=True)
    nominalnaya_nagruzka = models.CharField("Номинальная нагрузка", max_length=100, blank=True)
    ves = models.CharField("Вес", max_length=100, blank=True)

    class Meta:
        verbose_name = "Дождеприемник"
        verbose_name_plural = "Дождеприемники"


# --- Водоотводный лоток ---
class VodootvodnyyLotok(Product):
    naruzhnyy_razmer_lotka = models.CharField("Наружный размер лотка", max_length=100, blank=True)
    vysota = models.CharField("Высота", max_length=100, blank=True)
    nominalnaya_nagruzka = models.CharField("Номинальная нагрузка", max_length=100, blank=True)
    naruzhnyy_razmer_reshetki_lotka = models.CharField("Наружный размер решетки лотка", max_length=100, blank=True)
    ves = models.CharField("Вес", max_length=100, blank=True)

    class Meta:
        verbose_name = "Водоотводный лоток"
        verbose_name_plural = "Водоотводные лотки"


# --- Крышки ---
class Kryshki(Product):
    TIP_CHOICES = [
        ('Круглая', 'Круглая'),
        ('Квадратная', 'Квадратная'),
        ('Прямоугольная', 'Прямоугольная'),
    ]

    tip = models.CharField("Тип крышки", max_length=50, choices=TIP_CHOICES)
    razmer = models.CharField("Размер", max_length=100, blank=True)
    vysota = models.CharField("Высота", max_length=100, blank=True)
    nominalnaya_nagruzka = models.CharField("Номинальная нагрузка", max_length=100, blank=True)
    ves = models.CharField("Вес", max_length=100, blank=True)
    material = models.CharField("Материал", max_length=100, blank=True)

    class Meta:
        verbose_name = "Крышка"
        verbose_name_plural = "Крышки"


# --- Кольца ---
class Koltsa(Product):
    TIP_CHOICES = [
        ('Стеновое', 'Стеновое'),
        ('Опорное', 'Опорное'),
        ('Доборное', 'Доборное'),
    ]

    tip = models.CharField("Тип кольца", max_length=50, choices=TIP_CHOICES)
    vnutrenniy_diametr = models.CharField("Внутренний диаметр", max_length=100, blank=True)
    naruzhnyy_diametr = models.CharField("Наружный диаметр", max_length=100, blank=True)
    vysota = models.CharField("Высота", max_length=100, blank=True)
    ves = models.CharField("Вес", max_length=100, blank=True)
    material = models.CharField("Материал", max_length=100, blank=True)

    class Meta:
        verbose_name = "Кольцо"
        verbose_name_plural = "Кольца"


# --- Конусные переходы ---
class KonusnyePerehody(Product):
    diametr_verhniy = models.CharField("Верхний диаметр", max_length=100, blank=True)
    diametr_nizhniy = models.CharField("Нижний диаметр", max_length=100, blank=True)
    vysota = models.CharField("Высота", max_length=100, blank=True)
    tolshchina_stenki = models.CharField("Толщина стенки", max_length=100, blank=True)
    ves = models.CharField("Вес", max_length=100, blank=True)
    material = models.CharField("Материал", max_length=100, blank=True)

    class Meta:
        verbose_name = "Конусный переход"
        verbose_name_plural = "Конусные переходы"