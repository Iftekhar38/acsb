from django.contrib import admin
from .models import FeedbackModel
# Register your models here.

class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'message']


admin.site.register(FeedbackModel, FeedbackModelAdmin)