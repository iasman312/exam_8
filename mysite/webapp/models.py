from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
CHOICES = [
    ('laptop', 'Ноутбук'),
    ('smartphone', 'Смартфон'),
    ('food', 'Еда'),
]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    category = models.CharField(max_length=100, null=False, blank=False, choices=CHOICES, verbose_name='Категория')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    picture = models.ImageField(upload_to='product_pic', null=True, blank=True, verbose_name='Картинка')

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}'


class Feedback(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, related_name='feedbacks')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='feedbacks', verbose_name='Товар')
    feedback_text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст отзыва')
    rating = models.IntegerField(null=False, blank=False, default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    moderated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'feedbacks'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.feedback_text}'
