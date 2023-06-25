from django.shortcuts import render

from .models import Portfolio, Qualification ,Skill


# Create your views here.
def function(request):
    obj=Portfolio.objects.all()
    object=Qualification.objects.all()
    ob = Skill.objects.all()
    return render(request,"index.html",{'obj':obj,'object':object,'ob':ob})