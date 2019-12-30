from django.shortcuts import render
from .models import Contact


# Create your views here.
def home(request):
    return render(request, "index.html")


def thank(request):
    if request.method == "POST":
        your_name = request.POST.get("yourname")
        your_email = request.POST.get('youremail')
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        c = Contact(name=your_name, email=your_email, subject=subject, message=message)
        c.save()
        context = {"name": your_name, "email": your_email}
        return render(request, "thankyou.html", context=context)
    else:
        return render(request, "thankyou.html")
