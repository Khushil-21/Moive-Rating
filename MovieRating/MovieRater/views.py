from django.shortcuts import render
from django.http import HttpResponse
import json
import os

# Create your views here.
def MovieList(request):
    f = open(os.getcwd()+'\\MovieRater\\static\\data.json')
    data = json.load(f)
    f.close()
    return render(request,"MovieList.html",{"Alldata":data})

def MovieDetails(request,name):
    f = open(os.getcwd()+'\\MovieRater\\static\\data.json')
    data = json.load(f)
    f.close()
    for i in data:
        if name==i["title"]:
            selectedData=i
            break
    if selectedData:
        return render(request,"MovieDetails.html",{"selectedData":selectedData})
    else:
        return HttpResponse("Not Found")