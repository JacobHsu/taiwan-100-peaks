from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from peaks.models import Peak

class Command(BaseCommand):
    help = '載入台灣百岳基本資料'

    def handle(self, *args, **options):
        # 清除現有資料
        Peak.objects.all().delete()
        
        # 台灣百岳資料 (前10座)
        peaks_data = [
            {
                'name': '玉山主峰',
                'elevation': 3952,
                'latitude': 23.4703,
                'longitude': 120.9573,
                'difficulty': 'intermediate',
                'distance': 18.9,
                'duration_days': 2,
                'description': '台灣第一高峰，位於南投縣信義鄉、高雄市桃源區及嘉義縣阿里山鄉交界處。',
                'route_info': '排雲山莊路線，需申請入園證及山屋住宿。'
            },
            {
                'name': '雪山主峰',
                'elevation': 3886,
                'latitude': 24.3899,
                'longitude': 121.2265,
                'difficulty': 'intermediate',
                'distance': 21.5,
                'duration_days': 2,
                'description': '台灣第二高峰，素有「台灣屋脊」之稱，位於台中市和平區。',
                'route_info': '雪東線，369山莊過夜，景色壯麗。'
            },
            {
                'name': '玉山東峰',
                'elevation': 3869,
                'latitude': 23.4733,
                'longitude': 120.9630,
                'difficulty': 'advanced',
                'distance': 19.2,
                'duration_days': 2,
                'description': '玉山群峰之一，位於玉山主峰東側，景色壯麗。',
                'route_info': '由排雲山莊出發，技術性較高。'
            },
            {
                'name': '玉山北峰',
                'elevation': 3858,
                'latitude': 23.4861,
                'longitude': 120.9581,
                'difficulty': 'advanced',
                'distance': 20.1,
                'duration_days': 2,
                'description': '玉山群峰中技術難度最高的一座。',
                'route_info': '需要攀岩技巧，建議有經驗者挑戰。'
            },
            {
                'name': '玉山南峰',
                'elevation': 3844,
                'latitude': 23.4589,
                'longitude': 120.9542,
                'difficulty': 'intermediate',
                'distance': 22.3,
                'duration_days': 2,
                'description': '玉山群峰之一，路線較長但難度適中。',
                'route_info': '由排雲山莊經玉山主峰續行。'
            },
            {
                'name': '秀姑巒山',
                'elevation': 3825,
                'latitude': 23.4542,
                'longitude': 121.0264,
                'difficulty': 'advanced',
                'distance': 25.6,
                'duration_days': 3,
                'description': '中央山脈主脊上的重要山峰，景觀遼闊。',
                'route_info': '大水窟山屋路線，需3天行程。'
            },
            {
                'name': '馬博拉斯山',
                'elevation': 3785,
                'latitude': 23.5236,
                'longitude': 121.0431,
                'difficulty': 'expert',
                'distance': 28.4,
                'duration_days': 4,
                'description': '布農族聖山，位置偏遠，挑戰性極高。',
                'route_info': '需申請入園證，建議有豐富經驗者挑戰。'
            },
            {
                'name': '南湖大山',
                'elevation': 3742,
                'latitude': 24.3653,
                'longitude': 121.2292,
                'difficulty': 'intermediate',
                'distance': 23.7,
                'duration_days': 3,
                'description': '太魯閣國家公園內的著名山峰，有「帝王之山」美譽。',
                'route_info': '南湖山屋路線，風景優美。'
            },
            {
                'name': '中央尖山',
                'elevation': 3705,
                'latitude': 24.3847,
                'longitude': 121.2431,
                'difficulty': 'expert',
                'distance': 26.8,
                'duration_days': 3,
                'description': '有「寶島第一尖」之稱，攀登難度極高。',
                'route_info': '需要專業攀岩技術，僅適合專家級登山者。'
            },
            {
                'name': '丹大山',
                'elevation': 3703,
                'latitude': 23.6792,
                'longitude': 121.0542,
                'difficulty': 'advanced',
                'distance': 31.2,
                'duration_days': 4,
                'description': '位於南投縣信義鄉，路程遙遠但景色絕美。',
                'route_info': '七彩湖路線，需4天以上行程。'
            }
        ]

        # 建立山峰資料
        for peak_data in peaks_data:
            location = Point(peak_data['longitude'], peak_data['latitude'])
            
            peak = Peak.objects.create(
                name=peak_data['name'],
                elevation=peak_data['elevation'],
                location=location,
                difficulty=peak_data['difficulty'],
                distance=peak_data['distance'],
                duration_days=peak_data['duration_days'],
                description=peak_data['description'],
                route_info=peak_data['route_info']
            )
            
            self.stdout.write(
                self.style.SUCCESS(f'成功建立: {peak.name} ({peak.elevation}m)')
            )

        self.stdout.write(
            self.style.SUCCESS(f'成功載入 {len(peaks_data)} 座山峰資料！')
        )