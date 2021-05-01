from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import MyUserCreationForm


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('webapp:index')

    else:
        form = MyUserCreationForm()
    return render(request, 'user_create.html', context={'form': form})

