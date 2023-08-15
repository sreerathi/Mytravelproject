
from django.shortcuts import render
from.models import Place
from.models import Teams
# Create your views here.
def demo(request):
    objs=Place.objects.all()
    obj=Teams.objects.all()
    return render(request,"index.html",{'objs':objs,'obj':obj})