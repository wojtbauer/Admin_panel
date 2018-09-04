from django.contrib import admin

from SampleApp.models import SampleModel_1, SampleModel_2, Entry_1, Entry_2


# Register your models here.

admin.site.register(SampleModel_1)
admin.site.register(SampleModel_2)
admin.site.register(Entry_1)
admin.site.register(Entry_2)

