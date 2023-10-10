from django.shortcuts import render
from django.http import HttpResponse

def getinput(request):
    return render(request,template_name='get.html')
def postout(request):
    return render(request,template_name='post.html')
def add(request):
    print(request.method)
    if request.method == "GET":

        a=request.GET['t1']
        b=request.GET['t2']
        x=int(a)
        y=int(b)
        z=x+y
        return HttpResponse("this is the  final value :" +str(z))
    else:
        a=request.POST['t1']
        b=request.POST['t2']
        x=int(a)
        y=int(b)
        z=x+y
        return HttpResponse("this is the last value : "+str(z))