from django.db import models
# Temporarily remove PostGIS dependency for Render deployment
# from django.contrib.gis.db import models as gis_models

class Peak(models.Model):
    DIFFICULTY_CHOICES = [
        ('beginner', '初級'),
        ('intermediate', '中級'),
        ('advanced', '高級'),
        ('expert', '專家級'),
    ]
    
    STATUS_CHOICES = [
        ('incomplete', '未完成'),
        ('completed', '已完成'),
        ('planned', '計劃中'),
    ]

    # 基本資訊
    name = models.CharField('百岳名稱', max_length=100, unique=True)
    elevation = models.IntegerField('海拔高度 (公尺)')
    # Use simple decimal fields instead of PostGIS PointField
    latitude = models.DecimalField('緯度', max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField('經度', max_digits=10, decimal_places=7, null=True, blank=True)
    
    # 登山資訊
    difficulty = models.CharField('難度等級', max_length=20, choices=DIFFICULTY_CHOICES)
    distance = models.FloatField('來回距離 (公里)', null=True, blank=True)
    duration_days = models.IntegerField('預估天數', default=1)
    
    # 狀態追蹤
    status = models.CharField('完成狀態', max_length=20, choices=STATUS_CHOICES, default='incomplete')
    completion_date = models.DateField('完成日期', null=True, blank=True)
    planned_date = models.DateField('計劃日期', null=True, blank=True)
    
    # 詳細描述
    description = models.TextField('描述', blank=True)
    route_info = models.TextField('路線資訊', blank=True)
    notes = models.TextField('個人筆記', blank=True)
    
    # 時間戳記
    created_at = models.DateTimeField('建立時間', auto_now_add=True)
    updated_at = models.DateTimeField('更新時間', auto_now=True)

    class Meta:
        verbose_name = '台灣百岳'
        verbose_name_plural = '台灣百岳'
        ordering = ['-elevation']

    def __str__(self):
        return f"{self.name} ({self.elevation}m)"
