from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# resolve interface bug sticky-nav-bar
admin.autodiscover()
admin.site.enable_nav_sidebar = False


@admin.register(models.User)
class UserAdmin(UserAdmin):
	list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'phone_number')
	list_filter = ('groups',)
	search_fields = ('username', )
	fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number',)
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
	list_display = ('id', 'uploader',)
	list_filter = ('date_created',)


@admin.register(models.Club)
class ClubAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'address',)


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date',)
	list_filter = ('date_created',)
	search_fields = ('title', )


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ( 'category', 'level', 'coach', 'coach_adj',)
	list_filter = ('category', 'coach')
	search_fields = ('category',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	pass


@admin.register(models.Level)
class LevelAdmin(admin.ModelAdmin):
	pass
