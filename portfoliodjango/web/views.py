from django.shortcuts import render, redirect
from.forms import USerRegisterForm
from django.contrib import messages
# Create your views here.
def page_index(request):
    return render(request, "index.html")
def page_sign_in(request):
    return render(request, "sign-in.html")
def page_register(request):
    if request.method == "POST":
        form = USerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"usuario {username} creado")
            return redirect("/")
    else:
        form = USerRegisterForm()
    context = {"form": form}
    return render(request, "register.html", context)
def page_admin(request):
    return render(request, "admin.html")

