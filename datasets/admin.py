from django.contrib import admin
from .models import Dataset, Review, Tag, Japan, FoodWaste
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Dataset)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Japan, ImportExportModelAdmin)
admin.site.register(FoodWaste, ImportExportModelAdmin)


