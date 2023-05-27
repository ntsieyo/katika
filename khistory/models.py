from django.db import models
from person.models import Person
from mezzanine.core.fields import RichTextField
from mezzanine.utils.models import upload_to
from mezzanine.core.fields import FileField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from mezzanine.generic.fields import KeywordsField
from django.utils.text import slugify

from kthesis.models import unique_slug_max_length

import uuid


# https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html
# To study python manage.py migrate --fake core zero

class Personnage(Person):

    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # FORM Conf
    FORM_FIELDS = '__all__'
    FORM_EXCLUDE = ('featured_image',)

    class Meta:
        abstract = False






class Event(models.Model):

    date = models.DateField('date')
    importance = models.IntegerField(choices=((1, _("LOW")),
                                              (2, _("MEDIUM")),
                                              (3, _("HIGH"))),
                                     default=1)
    accuracy = models.IntegerField(choices=((1, _("DAY")),
                                            (2, _("MONTH")),
                                            (3, _("YEAR"))),
                                   default=1)

    title = models.TextField()
    content = RichTextField(blank=True, null=True)
    personnages = models.ManyToManyField(Personnage, blank=True, related_name='personnages')

    duration = models.DurationField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    image_credits = models.CharField(max_length=255, blank=True, null=True)
    image_caption = models.CharField(max_length=255, blank=True, null=True)
    featured_image = FileField(verbose_name=_("Featured Image"),
                               upload_to=upload_to("event.featured_image", "event"),
                               format="Image", max_length=255, null=True, blank=True)
    source = models.URLField(blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)

    reported_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    tags = KeywordsField()

    FORM_FIELDS = '__all_'
    FORM_EXCLUDE = ('personnage', 'featured_image', 'tags', 'reported_by', 'slug')


    def save(self, *args, **kwargs):

        if not self.slug:
            slug = self.title

            slug = slugify(slug)
            self.slug = unique_slug_max_length(Event.objects.all(), 'slug', slug, 255)

        super(Event, self).save(*args, **kwargs)
    # Keywords?

    def __str__(self):
        return "{}, {}".format(self.date, self.title)

    class Meta:
        verbose_name_plural = 'History events'  # ?
        ordering = ['-date']
