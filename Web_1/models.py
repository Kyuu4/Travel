from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50, help_text='не більше 20 символів')
    email = models.EmailField()
    phone = models.CharField(max_length=15, help_text='не більше 15 символів')
    message = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
"""
class Age(models.Model):
    age = models.IntegerField()

class Price(models.Model):
    price_month = models.IntegerField()
    price_lesson = models.IntegerField()
    date_price = models.IntegerField()#format 01012024(01.01.2024)
"""
class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                help_text='оберіть категорію',
                                verbose_name='категорія курсу', null = True)
    name = models.CharField(max_length=50, verbose_name='Ім\'я')
    kid_age = models.CharField(max_length=50, verbose_name='Вік учня', null=True)
    price = models.CharField(max_length=50, verbose_name='Вартість', null=True)
    date_price = models.IntegerField(verbose_name='Дата_ціна', null= True)
    image = models.ImageField(verbose_name='Картинка', upload_to="images_courses")
    description = models.CharField(max_length=100, verbose_name='Опис', null = True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reversed('course-detail', args = [str(self.id)])

    def display_age(self):
        return ', '.join([a.age for a in self.kid_age.all()])

    display_age.short_description = 'Вік'