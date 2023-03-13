from django.shortcuts import render

# Create your views here.

def first(request):
    d={'name':'Naveen','age':21}
    return render(request,'first.html',context=d)