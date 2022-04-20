from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital = models.BooleanField(default=False)
    slug = models.SlugField()
    main_image = models.ImageField(upload_to="posted_images/%Y/%m/%d/%H/%M")
    image1 = models.ImageField(upload_to="posted_images/%Y/%m/%d/%H/%M", blank=True, null=True)
    image2 = models.ImageField(upload_to="posted_images/%Y/%m/%d/%H/%M", blank=True, null=True)
    image3 = models.ImageField(upload_to="posted_images/%Y/%m/%d/%H/%M", blank=True, null=True)