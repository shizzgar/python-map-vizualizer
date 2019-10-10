from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Counter, Image
import image_slicer
import base64
import os
import io



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@shared_task(name = "imagetask.tasks.put_image")
def put_image(name, *args, **kwargs):

	counter = Counter.objects.all()[0]	
	if not counter:
		counter = Counter.objects.create(num=0)
	if counter.num > 133:
		counter.num = 0
	counter.num+=1
	counter.save()

	path_to_image = os.path.join(BASE_DIR, f'imagetask/images/data{counter.num}.png')
	tiles = image_slicer.slice(path_to_image, 100, save=False)
	i = 0
	for tile in tiles:
		i+=1
		with io.BytesIO() as data:
			# filename = tile.generate_filename(path=False)
			tile.save(data)
			data.seek(0,0)
			readed_data = data.read()
			base_data = base64.b64encode(readed_data)
			img, created = Image.objects.get_or_create(name = i)		
			img.data = base_data
			img.save()

	print(f'Image {counter.num} stored to DB by {name}')
