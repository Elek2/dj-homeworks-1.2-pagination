from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv



def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    bus_file = open(settings.BUS_STATION_CSV, encoding='utf-8')
    reader = list(csv.DictReader(bus_file, delimiter=","))
    paginator = Paginator(reader, 10)
    page_num = request.GET.get("page", 1)
    page = paginator.get_page(page_num)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

