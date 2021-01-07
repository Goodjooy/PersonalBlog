from datetime import date
from django.db import models
from django.db.models.fields.files import ImageField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Artical(models.Model):

    title = models.CharField(max_length=50, default="Empty")
    postData = models.DateField("data publish")
    readCount = models.IntegerField(default=0)


    text = models.FileField(upload_to="articials/%Y-%m/",max_length=250)

    class Meta:
        verbose_name = ("artical")
        verbose_name_plural = ("articals")

    def __str__(self):
        return self.title

    def is_post(self):
        """
        检查是否需要发送
        """
        return self.postData<= date(timezone.now())


class Image(models.Model):

    date=models.DateField()
    src=models.ImageField(upload_to="images/%Y-%m/",max_length=250)
    

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        return self.date.ctime()

   