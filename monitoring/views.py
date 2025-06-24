from django.shortcuts import render
from .models import PoliceStation, CCTV, CCTVArea
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import CCTVArea
from django.db.models import Count

@login_required
def dashboard(request):
    ps_count = PoliceStation.objects.count()
    cctv_count = CCTV.objects.filter(is_active=True).count()
    locations = CCTV.objects.filter(is_active=True)

    return render(request, 'dashboard.html', {
        'ps_count': ps_count,
        'cctv_count': cctv_count,
        'locations': locations,
    })

@login_required
def map_page(request):
    stations = PoliceStation.objects.all()
    return render(request, 'map_page.html', {'stations': stations})

@login_required
def station_cctvs(request, ps_id):
    station = PoliceStation.objects.get(id=ps_id)
    cctvs = CCTV.objects.filter(cctv_area__police_station=station, latitude__isnull=False, longitude__isnull=False)
    return render(request, 'cctv_list_map.html', {'cctvs': cctvs, 'station': station})

@login_required
def area_list_view(request, ps_id):
    station = PoliceStation.objects.get(id=ps_id)
    areas = CCTVArea.objects.filter(police_station=station).prefetch_related('cctvs')
    return render(request, 'area_list.html', {'station': station, 'areas': areas})


@login_required
def cctv_area_map(request, area_id):
    area = get_object_or_404(CCTVArea, id=area_id)
    cctvs = area.cctvs.filter(latitude__isnull=False, longitude__isnull=False)
    return render(request, 'cctv_area_map.html', {'area': area, 'cctvs': cctvs})

@login_required


def area_dashboard(request):
    areas = (
        CCTVArea.objects
        .annotate(total_cctvs=Count('cctvs'))  # aggregate related cctvs
        .distinct()
        .order_by('police_station__name', 'name')
    )
    return render(request, 'area_dashboard.html', {'areas': areas})



@login_required
def station_cctvs(request, ps_id):
    station = get_object_or_404(PoliceStation, id=ps_id)
    cctvs = CCTV.objects.filter(cctv_area__police_station=station)
    return render(request, 'cctv_list_map.html', {
        'station': station,
        'cctvs': cctvs,
    })

def custom_permission_denied(request, exception=None):
    return render(request, '403.html', status=403)
