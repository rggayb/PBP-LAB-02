from django.shortcuts import render
from katalog.models import CatalogItem
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()

    context = {
    'list_barang': data_barang_katalog,
    'name': 'Rangga Yudhistira',
    'NPM' : '2106751051'
}
    return render(request, "katalog.html", context)