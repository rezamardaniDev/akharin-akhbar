from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True, verbose_name="تگ")
    url = models.CharField(max_length=250, null=True, blank=True, verbose_name="لینک تگ")

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True, verbose_name="دسته بندی")
    url = models.CharField(max_length=250, null=True, blank=True, verbose_name="لینک دسته بندی")

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True, verbose_name="عنوان خبر")
    short_description = models.TextField(blank=True, null=True, verbose_name="توضیحات کوتاه")
    description = models.TextField(blank=True, null=True, verbose_name="متن خبر")
    author = models.CharField(max_length=250, null=True, verbose_name="نویسنده خبر")
    created_date = jmodels.jDateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, verbose_name="تگ خبر")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")
    status = models.BooleanField(default=False, verbose_name="فعال/غیرفعال")
    selected = models.BooleanField(default=False, verbose_name="خبر برگزیده")
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title