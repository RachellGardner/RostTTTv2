from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class ProductImage(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name="Тип объекта")
    object_id = models.PositiveIntegerField(verbose_name="ID объекта", db_index=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    image = models.ImageField("Изображение", upload_to='product_images/')
    created_at = models.DateTimeField("Добавлено", auto_now_add=True)

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

    def __str__(self):
        return f"Изображение для {self.content_object.name if self.content_object else 'неизвестного'}"


class Product(models.Model):
    name = models.CharField("Название", max_length=200, db_index=True)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Основное изображение", upload_to='products/', null=True, blank=True)
    specifications = models.TextField("Общие характеристики", blank=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def get_specifications(self):
        specs = []

        if self.specifications:
            specs.append(self.specifications)

        skip_fields = {'id', 'created_at', 'name', 'description', 'image', 'specifications'}

        for field in self._meta.get_fields():
            if not isinstance(field, models.Field) or field.name in skip_fields:
                continue

            value = getattr(self, field.name, None)
            if not value:
                continue

            label = getattr(field, 'verbose_name', field.name)
            if hasattr(field, 'choices') and field.choices:
                value = dict(field.choices).get(value, value)

            specs.append(f"{label}: {value}")

        return specs


# ========== Товары ==========

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


class VodootvodnyyLotok(Product):
    naruzhnyy_razmer_lotka = models.CharField("Наружный размер лотка", max_length=100, blank=True)
    vysota = models.CharField("Высота", max_length=100, blank=True)
    nominalnaya_nagruzka = models.CharField("Номинальная нагрузка", max_length=100, blank=True)
    naruzhnyy_razmer_reshetki_lotka = models.CharField("Размер решетки", max_length=100, blank=True)
    ves = models.CharField("Вес", max_length=100, blank=True)

    class Meta:
        verbose_name = "Водоотводный лоток"
        verbose_name_plural = "Водоотводные лотки"


class Kryshki(Product):
    TIP_CHOICES = [
        ('Полимерно-песчаный', 'Полимерно-песчаный'),
        ('Дно колодца', 'Дно колодца'),
       
    ]

    tip = models.CharField("Тип колодца", max_length=50, choices=TIP_CHOICES)
    razmer = models.CharField("Наружный диаметр", max_length=100, blank=True)
    vysota = models.CharField("Высота", max_length=100, blank=True)
    nominalnaya_nagruzka = models.CharField("Вес", max_length=100, blank=True)
    ves = models.CharField("Вес", max_length=100, blank=True)
    material = models.CharField("Материал", max_length=100, blank=True)

    class Meta:
        verbose_name = "Колодец"
        verbose_name_plural = "Колодца"


class Koltsa(Product):
    TIP_CHOICES = [
        ('Стеновое', 'Стеновое'),
        ('Опорное', 'Опорное'),
        ('Для Колодца', 'Для Колодца'),
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


class KonusnyePerehody(Product):
    diametr_verhniy = models.CharField("Наружный размер", max_length=100, blank=True)
    diametr_nizhniy = models.CharField("Внутренний диаметр", max_length=100, blank=True)
    vysota = models.CharField("Высота", max_length=100, blank=True)
    tolshchina_stenki = models.CharField("Толщина крышки", max_length=100, blank=True)
    ves = models.CharField("Вес", max_length=100, blank=True)
    material = models.CharField("Номинальная нагрузка", max_length=100, blank=True)

    class Meta:
        verbose_name = "Конусный переход"
        verbose_name_plural = "Конусные переходы"
