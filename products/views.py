from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Product, Forum, DemoPic
from .forms import ProductForm
from django.contrib import messages
from .forms import OurForum


def home(request):
    #products = Product.objects.filter(active=False)
    #products = Product.objects.order_by('-updated')
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'products/home.html', context)

def detail(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        context = {'product':product}
    except Product.DoesNotExist:
        raise Http404
    return render(request, 'products/detail.html', context)

def delete(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == "POST":
        product.delete()
        messages.warning(request, 'Product deleted from database..')
        return redirect('products:home')
    return render(request, 'products/delete.html', {'product':product})

def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product creation Succssfull!!')
            return redirect('products:home')
    else:
        form = ProductForm()
    return render(request, 'products/create_form.html', {'form': form })

def update(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == "POST":
        form = ProductForm(request.POST or None, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, 'Product Updation Succssfull!!')
            return redirect('products:home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/update.html', {'form':form})

def our_forum(request):
    if request.method == "POST":
        form = OurForum(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            address_1 = form.cleaned_data['address_1']
            address_2 = form.cleaned_data['address_2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zip = form.cleaned_data['zip']
            check_me_out = form.cleaned_data['check_me_out']
            object = Forum(email=email, name=name, address_1=address_1,
                           address_2=address_2, city=city, state=state,
                           zip = zip, check_me_out=check_me_out)
            object.save()
            return HttpResponse('<h2>Thanks for submitting info..</h2>')
    else:
        form = OurForum()
    return render(request, 'products/forum.html', {'form':form})


def demo_pic(request):
    return render(request, 'products/demo.html', {'pic':DemoPic.objects.first()})
