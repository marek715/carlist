from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    car_make = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200)
    car_price = models.PositiveIntegerField()
    car_lease = models.PositiveIntegerField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url():
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.car_model
