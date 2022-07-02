from django.shortcuts import render

# Create your views here.
from blog.forms import MebelForm
from blog.models import Mebel, OurBrand, Logo, Mebelforma


def mebel(request):
    mebel = Mebel.objects.all()
    brand = OurBrand.objects.all()
    logo = Logo.objects.all()
    context = {
        'mebel':mebel,
        'brand': brand,
        'logo': logo,
    }
    return render(request,'home.html',context)

def about_detail(request,pk):
    mebel = Mebel.objects.get(pk=pk)
    form = MebelForm(request.POST or None)
    is_success = False
    if request.method == 'POST' and form.is_valid():
        is_success = True
        form.save()
        form = MebelForm()

    context = {
        'mebel': mebel,
        'form': form,
    }
    return render(request,'about_detail.html',context)