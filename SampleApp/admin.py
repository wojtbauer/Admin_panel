from django.contrib import admin

from SampleApp.models import SampleModel, Entry


# Register your models here.

admin.site.register(SampleModel)
admin.site.register(Entry)


