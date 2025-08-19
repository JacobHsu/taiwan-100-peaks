from django.contrib import admin
# Remove PostGIS dependency for Render deployment
# from django.contrib.gis.admin import GeoModelAdmin
from .models import Peak

@admin.register(Peak)
class PeakAdmin(admin.ModelAdmin):
    list_display = ['name', 'elevation', 'difficulty', 'status', 'completion_date']
    list_filter = ['difficulty', 'status', 'duration_days']
    search_fields = ['name', 'description']
    list_editable = ['status']
    ordering = ['-elevation']
    
    fieldsets = (
        ('基本資訊', {
            'fields': ('name', 'elevation', 'latitude', 'longitude')
        }),
        ('登山資訊', {
            'fields': ('difficulty', 'distance', 'duration_days')
        }),
        ('狀態追蹤', {
            'fields': ('status', 'completion_date', 'planned_date')
        }),
        ('詳細資訊', {
            'fields': ('description', 'route_info', 'notes'),
            'classes': ('collapse',)
        }),
    )
