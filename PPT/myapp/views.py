from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    searchTerm=request.GET.get('textbox')
#textbox means the name of the input type.
    movies=Movie.objects.all()
    return render(request,'home.html',{'XYZ':XYZ,'searchTerm':searchTerm,'movies':movies})
def room(request):
    return render(request,'room.html',{'XZZ':XZZ})
XYZ=[
    {'subject':'FSCP-2','faculty':'PKV'},
    {'subject':'FSD-2','faculty':'ZMP'},
    {'subject':'DM','faculty':'FRT'},
]
XZZ=[
    {'subject':'TOC','faculty':'KJP'},
    {'subject':'COA','faculty':'VBY'},
    {'subject':'INTERNSHIP','faculty':'MKP'},
]