from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout

# Create your views here.
def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"You are now successfully register as {username}")
            return redirect('login')

    context={
        'form': form,
    }

    return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required(login_url='login')
def profilepage(request):
    return render(request, 'users/profile.html')
