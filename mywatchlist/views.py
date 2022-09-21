from django.shortcuts import render
from mywatchlist.models import MyWatchlistItem
from django.http import HttpResponse
from django.core import serializers


# TODO: Create your views here.
def show_mywatchlist(request):
    item_mywatchlist = MyWatchlistItem.objects.all()
    belum_nonton = 0
    watched = 0
    pesan = ""

    for movies in item_mywatchlist:
        if(movies.watched):
            watched +=1
        else:
            belum_nonton += 1

    print (belum_nonton)
    if (watched >= belum_nonton):
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan  = "Wah, kamu masih sedikit menonton!"

    context = {
        'item_mywatchlist': item_mywatchlist,
        'nama' : 'Rangga Yudhistira',
        'pesan' : pesan,
    }
    return render(request, 'mywatchlist.html', context)

def show_xml(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    data = MyWatchlistItem.objects.all()
    context = {
        'item_mywatchlist': data,
        'nama' : 'Rangga Yudhistira',
    }
    return render(request, 'mywatchlist.html', context)