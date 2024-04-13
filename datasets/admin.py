from django.contrib import admin
from .models import Dataset, Review, Tag, Japan

# Register your models here.
admin.site.register(Dataset)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Japan)
