from django.db import models


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


# --- Тротуарная плитка ---
class TrotuarnayaPlitka(Product):
    razmery = models.CharField("Размеры", max_length=100, blank=True)
    vysota = models.CharField("Высота", max_length=100, blank=True)
    kolichestvo_na_km = models.CharField("Количество на 1 к.м", max_length=100, blank=True)

    class Meta:
        verbose_name = "Тротуарная плитка"
        verbose_name_plural = "Тротуарная плитка"


# --- Черепица ---
class Cherepitsa(Product):
    razmer_gabaritnyy_ryadnoy = models.CharField("Размеры (габаритные) рядной черепицы", max_length=100, blank=True)
    razmer_kroynoy_ryadnoy = models.CharField("Размер (кроющий) рядной черепицы", max_length=100, blank=True)
    razmer_gabaritnyy_konkovoy = models.CharField("Размер (габаритные) коньковой черепицы", max_length=100, blank=True)
    razmer_kroynoy_konkovoy = models.CharField("Размер (кроющей) коньковой черепицы", max_length=100, blank=True)
    massa_ryadnoy = models.CharField("Масса рядной черепицы", max_length=100, blank=True)
    chislo_ryadnoy_na_kvadrat = models.CharField("Число черепицы на 1 кв.м (рядной)", max_length=100, blank=True)
    chislo_konkovoy_na_kvadrat = models.CharField("Число черепицы на 1 кв.м (коньковой)", max_length=100, blank=True)
    temperaturnyy_diapazon = models.CharField("Температурный диапазон", max_length=100, default="от -60 до +120")

    class Meta:
        verbose_name = "Черепица"
        verbose_name_plural = "Черепица"

        