from django.contrib import admin
from logistic.models import Logistic


class LogisticAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Logistic, LogisticAdmin)