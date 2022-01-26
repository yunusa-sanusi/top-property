from tabnanny import verbose
from django.db import models
from agents.models import Agent
from autoslug import AutoSlugField


class Property(models.Model):
    class Meta:
        verbose_name_plural = 'Properties'

    class PropertyType(models.TextChoices):
        AGRICULTURAL = 'agricultural', 'Agricultural'
        COMMERCIAL = 'commercial', 'Commercial'
        INDUSTRIAL = 'industrial', 'Industrial'
        RESIDENTIAL = 'residential', 'Residential'
        SPECIAL_USE = 'special use', 'Special Use'

    class Status(models.TextChoices):
        RENT = 'rent', 'Rent'
        SALE = 'sale', 'Sale'

    agent = models.ForeignKey(
        Agent, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, unique=True)
    city = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=10)
    description = models.TextField()
    price = models.CharField(max_length=20)
    beds = models.IntegerField()
    baths = models.IntegerField()
    garage = models.IntegerField()
    area = models.IntegerField()
    property_picture = models.ImageField(upload_to='images/property_images')
    video = models.FileField(
        upload_to='videos/property_videos/', null=True, blank=True)
    property_type = models.CharField(
        'PropertyType', max_length=30, choices=PropertyType.choices, default=PropertyType.RESIDENTIAL)
    status = models.CharField('Status', max_length=10,
                              choices=Status.choices, default=Status.SALE)
    slug = AutoSlugField(unique=True, always_update=True,
                         populate_from='address')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    @property
    def video_url(self):
        try:
            video = self.video.url
        except:
            video = ''
        return video

    @property
    def image_url(self):
        try:
            image = self.property_picture.url
        except:
            image = ''
        return image

    def __str__(self):
        return f'{self.agent} - {self.address}'


class PropertyImage(models.Model):
    class Meta:
        verbose_name_plural = 'Property Images'

    property = models.ForeignKey(
        'Property', on_delete=models.CASCADE, null=True, related_name='property_images')
    image = models.ImageField(upload_to='images/property-images/')

    def image_url(self):
        try:
            image = self.image.url
        except:
            image = ''
        return image

    def __str__(self):
        return f'Image for {self.property}'


class Amenity(models.Model):
    class Meta:
        verbose_name_plural = 'Amenities'

    property = models.ForeignKey(
        'Property', on_delete=models.CASCADE, null=True, related_name='property_amenities')
    amenity = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.amenity}'
