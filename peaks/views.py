from django.shortcuts import render
from .models import Peak

def home(request):
    # 從資料庫獲取山峰資料
    peaks = Peak.objects.all()
    
    context = {
        'peaks': peaks
    }
    
    return render(request, 'home.html', context)
