from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'Masala Latte'),
        ('CL', 'Chai Latte'),
        ('TL', 'Turmeric Latte'),
        ('GL', 'Ginger Latte'),
        ('HL', 'Honey Latte'),
        ('OL', 'Oat Latte'),
        ('AL', 'Almond Latte'),
        ('CL', 'Coconut Latte'),
        ('SL', 'Spiced Latte'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai_images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)

    def __str__(self):
        return self.name
