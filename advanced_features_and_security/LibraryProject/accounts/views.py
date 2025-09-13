from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in immediately after registration
            return redirect("home")  # change "home" to your homepage url name
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

