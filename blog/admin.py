from django.contrib import admin
from django.contrib import admin
from .models import Topic

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    fields = ('name', 'description', 'symptoms', 'cause', 'prevention', 'treatment')
