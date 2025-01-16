from django.contrib import admin

# Register your models here.
from django import template
from .template_tags.chunks import *
from .template_tags import chunks
from . models import movie
# Register your models here.
admin.site.register(movie)

from .template_tags import chunks
template.Library.tag(self=chunks,name='chunks')


