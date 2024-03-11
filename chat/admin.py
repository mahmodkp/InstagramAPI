from django.contrib import admin
from .models import DirectMessage
# Register your models here.


@admin.register(DirectMessage)
class DirectMessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sender',
        'receiver',
        'content_type',
        'content',
        'text_content',
        'created_at',
    )
    
    search_fields = (
        'text_content',
    )
