from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.success(request, f"Your account has been created: {username}")
            return redirect('products:home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
