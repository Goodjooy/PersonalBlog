from datetime import date
from django.db import models
from django.utils import timezone
# Create your models here.


class Artical(models.Model):

    title = models.CharField(max_length=50, default="Empty")
    postData = models.DateField("data publish")
    readCount = models.IntegerField(default=0)

    text = models.CharField(max_length=100)

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
