from django.shortcuts import render

def home(request):
    # Sample data for Taiwan 100 peaks
    peaks_data = [
        {
            'id': 1,
            'name': '玉山主峰',
            'status': '中部',
            'distance': '18.9 km',
            'elevation': '3952 m',
            'latitude': 23.4703,
            'longitude': 120.9573,
            'description': '台灣第一高峰，位於南投縣信義鄉、高雄市桃源區及嘉義縣阿里山鄉交界處。'
        },
        {
            'id': 2,
            'name': '雪山主峰', 
            'status': '北部',
            'distance': '21.5 km',
            'elevation': '3886 m',
            'latitude': 24.3899,
            'longitude': 121.2265,
            'description': '台灣第二高峰，素有「台灣屋脊」之稱，位於台中市和平區。'
        },
        {
            'id': 3,
            'name': '玉山東峰',
            'status': '中部', 
            'distance': '19.2 km',
            'elevation': '3869 m',
            'latitude': 23.4733,
            'longitude': 120.9630,
            'description': '玉山群峰之一，位於玉山主峰東側，景色壯麗。'
        }
    ]
    
    context = {
        'peaks': peaks_data
    }
    
    return render(request, 'home.html', context)
