from django.db import models

# Create your models here.
class Sites(models.Model):
    date_value = models.DateField()
    A_value = models.DecimalField(max_digits=10, decimal_places=2)
    B_value = models.DecimalField(max_digits=10, decimal_places=2)
    site_name = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        super(Sites, self).save(*args, **kwargs)
