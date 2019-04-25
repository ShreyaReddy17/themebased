from django.http import HttpResponse
from django.shortcuts import render
from .models import College

def index(request):
    all_colleges = College.objects.all()
   # context = { 'all_albums': all_albums, }
    return render(request, 'colleges/index.html',{ 'all_colleges': all_colleges })

def detail(request,college_id):
    try:
        college =College.objects.get(pk=college_id)
    except College.DoesNotExist:
        raise Http404("College does not exist")
    return render(request, 'colleges/detail.html' , {'college' : college })

def basicinfo(request,college_id):
    college =College.objects.get(pk=college_id)
    return render(request, 'colleges/detail.html' , {'college' : college })

def course(request,college_id):
    college =College.objects.get(pk=college_id)
    return render(request, 'colleges/course.html' , {'college' : college })

def reviews(request,college_id):
    college =College.objects.get(pk=college_id)
    return render(request, 'colleges/reviews.html' , {'college' : college })

def facilities(request,college_id):
    college =College.objects.get(pk=college_id)
    return render(request, 'colleges/facilities.html' , {'college' : college })

def gallery(request,college_id):
    college =College.objects.get(pk=college_id)
    return render(request, 'colleges/gallery.html' , {'college' : college })    
def contact(request,college_id):
    college =College.objects.get(pk=college_id)
    return render(request, 'colleges/contact.html' , {'college' : college })    

