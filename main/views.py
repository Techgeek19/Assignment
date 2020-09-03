from django.shortcuts import render, HttpResponse
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect) 


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/api/v1/calculate") 
    else:
        return render(request, 'index.html')

def calc(request):
    return render(request, 'calc1.html')

def sol(request):
    val1 = int(request.GET.get("num1"))
    val2 = int(request.GET.get("num2"))
    s = 0.00  
    for i in range(1, val2+1): 
        s += 1/val1**i
    sum=round(s,2)
    print(sum)
    return render(request, 'calc.html', {'sum':sum})
