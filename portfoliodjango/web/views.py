from django.shortcuts import render
# Create your views here.
def page_index(request):
    return render(request, "index.html")
def page_sign_in(request):
    return render(request, "sign-in.html")
def page_register(request):
    return render(request, "register.html")
def page_admin(request):
    return render(request, "admin.html")

