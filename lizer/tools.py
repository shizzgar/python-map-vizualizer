# from django.test import TestCase

# Create your tests here.
import os
import pyproj
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lizer.settings')
app = Celery('lizer')
app.config_from_object('django.conf:settings', namespace='CELERY')
import django
django.setup()
app.autodiscover_tasks()
from imagetask.projection import Projection
from imagetask.models import Image
from django.contrib.gis.geos import Polygon, Point


def init_polygons(*args, **kwargs):
    projection = Projection(geod=pyproj.Geod(ellps='WGS84'),start_lat=37.395,start_lon=55.9146,scaleX=39.8, scaleY=88.5) #37.3151 55.9146
    i = 0
    for y in range(0, 1000, 100):
        for x in range(0,1000,100):
            i+=1
            con1 = [-x,-y]
            con2 = [-x+100,-y]
            con3 = [-(x-100),-(y+100)]
            con4 = [-x,-(y+100)]
            point1 = Point(projection.to_latlon(con1[1],con1[0]))
            point2 = Point(projection.to_latlon(con2[1],con2[0]))
            point3 = Point(projection.to_latlon(con3[1],con3[0]))
            point4 = Point(projection.to_latlon(con4[1],con4[0]))
            poly = Polygon((point1.coords,point2.coords,point3.coords,point4.coords,point1.coords))

            # num_x = int(x/100)+1
            # num_y = int(y/100)+1
            # if num_x < 10:
            #     name_x = f'0{num_x}'
            # else:
            #     name_x = f'{num_x}'

            # if num_y < 10:
            #     name_y = f'0{num_y}'
            # else:
            #     name_y = f'{num_y}'

            img, created = Image.objects.get_or_create(name = i)#f'tile_{name_x}_{name_y}.png')
            img.square = poly
            img.save()
            print(poly, created, img)
