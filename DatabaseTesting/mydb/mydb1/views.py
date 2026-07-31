from django.shortcuts import render

# Create your views here.
def all_data(req):
    return render(req,"salespeople/all.html")