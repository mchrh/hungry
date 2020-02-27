from django.db import models

class results(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    ING1=models.CharField(max_length=100)
    ING2 = models.CharField(max_length=100)
    ING3 = models.CharField(max_length=100)
    ING4 = models.CharField(max_length=100)
    ING5 = models.CharField(max_length=100)
    CATEGORY=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural="recipes"

    def __str__(self):
        return self.name



