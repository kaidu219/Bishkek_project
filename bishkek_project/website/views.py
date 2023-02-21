from django.shortcuts import render
from .models import News, About_city

# Create your views here.
def index(request):
    news = News.objects.all().order_by('-time_news')
    about_city = About_city.objects.all()
    context = {
        'news': news,
        'about_city' : about_city,
    }
    return render(request, 'website/index.html', context=context)

def contact(request):
    return render(request, 'website/contactus.html')

def about(request):
    return render(request, 'website/aboutus.html')

