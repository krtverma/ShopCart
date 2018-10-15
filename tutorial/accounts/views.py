from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm

def home(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/login.html', {'form': form})
