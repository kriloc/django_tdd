from django.db import models

# Create your models here.
class Item(models.Model):
    text = models.TextField(default='')

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "itemss"

    def __str__(self):
        return self.text  # 這樣在admin 頁面才會顯示object name