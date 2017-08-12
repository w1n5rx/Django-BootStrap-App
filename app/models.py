from django.db import models

# Create your models here.
class Sites(models.Model):
    date_value = models.DateField()
    A_value = models.FloatField()
    B_value = models.FloatField()
    site_name = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        super(Sites, self).save(*args, **kwargs)

# data = Sites(date_value='Feb. 1, 2015', A_value=12.00, B_value=16.00, site_name='Demo Site')
# data.save()
# Sites.objects.bulk_create([
#     Sites(date_value='Feb. 1, 2015', A_value=12.00, B_value=16.00, site_name='Demo Site'),
#     Sites(date_value='Feb. 3, 2015', A_value=20.00, B_value=100.00, site_name='Demo Site'),
#     Sites(date_value='Feb. 10, 2015', A_value=20.00, B_value=80.00, site_name='Demo Site'),
#     Sites(date_value='Feb. 3, 2015', A_value=5.00, B_value=15.00, site_name='ABC Site'),
#     Sites(date_value='Feb. 15, 2015', A_value=5.00, B_value=15.00, site_name='XYZ Site'),
#     Sites(date_value='Feb. 28, 2015', A_value=5.00, B_value=15.00, site_name='XYZ Site'),
# ])