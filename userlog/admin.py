from django.contrib import admin

# Register your models here.

from .models import *



class PostLogAdmin(admin.ModelAdmin):
    """
    Category admin page
    """
    list_display = [
        "user",
        "post",
        "action",

    ]
    #search_fields = ["user", "caption"]
    # ordering = ["name"]
    # list_filter = ["is_active"]
    # list_editable = ["is_active"]
    list_per_page = 30

    # actions = ["make_active", "make_not_active"]

    # @admin.action(description="Mark selected comments as active")
    # def make_active(self, request, queryset):
    #     queryset.update(is_active=True)

    # @admin.action(description="Mark selected comments as not active")
    # def make_not_active(self, request, queryset):
    #     queryset.update(is_active=False)
    inlines = (
        # HashtagInline,
    )
class StoryLogAdmin(admin.ModelAdmin):
    """
    Category admin page
    """
    list_display = [
        "user",
        "story",
        "action",

    ]
    #search_fields = ["user", "caption"]
    # ordering = ["name"]
    # list_filter = ["is_active"]
    # list_editable = ["is_active"]
    list_per_page = 30

    # actions = ["make_active", "make_not_active"]

    # @admin.action(description="Mark selected comments as active")
    # def make_active(self, request, queryset):
    #     queryset.update(is_active=True)

    # @admin.action(description="Mark selected comments as not active")
    # def make_not_active(self, request, queryset):
    #     queryset.update(is_active=False)
    inlines = (
        # HashtagInline,
    )


admin.site.register(PostLog, PostLogAdmin)
admin.site.register(StoryLog, StoryLogAdmin)

