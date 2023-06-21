from django.shortcuts import render

# Create your views here.
def cdn_boostrap(request):
    return render(request,'cdn_boostrap.html')