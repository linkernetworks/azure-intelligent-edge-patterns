"""App admin.
"""

from django.contrib import admin

from .models import PredictionModule

# Register your models here.
admin.site.register(PredictionModule)
