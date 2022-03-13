import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=50)
    slug = models.SlugField(verbose_name=_("Slug"), unique=True)
    description = models.TextField(blank=True, null=True)
    metadata = models.JSONField(verbose_name=_("Metadata"), blank=True, null=True, help_text=_("Metadata about city."))

    def __str__(self):
        return self.city


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    profile_city = models.ForeignKey(City, verbose_name=_('Preferred City'), null=True, on_delete=models.CASCADE)
    preferred_contact = models.CharField(max_length=30, null=True, verbose_name=_('Preferred Contact'))
    metadata = models.JSONField(verbose_name=_("Metadata"), blank=True, null=True,
                                help_text=_("Metadata about profile."))

    def __str__(self):
        return str(self.user)


class ListingType(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(verbose_name=_("Slug"), unique=True)
    parent = models.ForeignKey("self", null=True, blank=True, related_name='subcat', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    listing_city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(ListingType, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to="listing_photos", null=True, blank=True, verbose_name=_("Listing Photo"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    metadata = models.JSONField(verbose_name=_("Metadata"), blank=True, null=True,
                                help_text=_("Metadata about listing."))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return "/media/listing_photos/classifieds-default.jpg"


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance")
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender='auth.User')
def create_token(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Token.objects.create(user=instance)
