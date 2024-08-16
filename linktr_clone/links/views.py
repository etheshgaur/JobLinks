from .models import Profile
import profile
from django.shortcuts import get_object_or_404, redirect, render
from .models import Link

def home(request):
  
    links = Link.objects.all()
    for link in links:
        link.visit_count += 1
        link.save()
    profile = Profile.objects.first() 
    return render(request, 'links/index.html', {'links': links, "profile": profile})

def link_click(request, link_id):
    link = get_object_or_404(Link, id=link_id)
    link.click_count += 1
    link.save()
    return redirect(link.url)