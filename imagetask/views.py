from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .models import Image
import base64
import io 
from PIL import Image as Img

# Create your views here.

def index(request):
    context = {}
    return render(request, 'map.html', context)


def img_display(request):
    response = []
    imgs = Image.objects.all()
    for img in imgs:
        data = img.data.tobytes()
        dec_data = data.decode('ascii')

        # buf = io.BytesIO(base64.b64decode(data))
        # trans_img = Img.open(buf)
        # trans_img=trans_img.convert('RGBA')
        # alpha = Img.new("L", trans_img.size, color = 128)
        # trans_img.putalpha(alpha)
        # bytes_trans_img= trans_img.tobytes()
        # trans_pic = base64.b64encode(bytes_trans_img) 

        pic = 'data:image/png;base64,{}'.format(dec_data)
        coords = img.square.coords[0]
        bounds = [[coords[2][1],coords[2][0]],[coords[0][1],coords[0][0]]]
        resp = {'pic':pic,'bounds':bounds}
        response.append(resp) 
    return JsonResponse(response, safe=False) 

