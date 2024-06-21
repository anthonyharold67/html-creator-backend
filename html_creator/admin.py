# Register your models here.
from django.contrib import admin
from import_export.admin import ExportMixin
from .models import HtmlCreatorModel
from django.contrib.admin.filters import DateFieldListFilter
from import_export.formats import base_formats

class HtmlCreatorAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('entity_id', 'created_at', 'last_updated')
    list_filter = (
        ('created_at', DateFieldListFilter),
        ('last_updated', DateFieldListFilter),
        # Diğer filtreleriniz
    )
    # Eğer özelleştirilmiş bir dışa aktarma formatı istiyorsanız, bu ayarı yapın
    formats = [base_formats.XLSX, base_formats.CSV]

admin.site.register(HtmlCreatorModel, HtmlCreatorAdmin)
