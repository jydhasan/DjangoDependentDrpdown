from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

from ajax.forms import ProductForm
from .models import Category, SubCategory

# Create your views here.
def home(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Invalid Form..")
    
    return render(request,'home.html',{
        'form':form
    })
    
def loadsubcat(request):
    cat_id = request.GET.get('cat_id')
    print(cat_id)
    
    sub_cats = SubCategory.objects.filter(category_id = cat_id)
    print(sub_cats)
    return render(request,'sub_cats.html',{
        'sub_cats':sub_cats
    })
    
