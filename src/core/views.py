from django.shortcuts import render
from apps.visits.models import PageVisit


def home(request, *args, **kwargs):
    total_visit = PageVisit.objects.all().count()
    page_visit = PageVisit.objects.filter(path=request.path).count()
    # print('Path', request.path)
    PageVisit.objects.create(path=request.path)
    return render(request, "home.html", 
                  {
                      "title":"Home Page",
                      "page_visit":page_visit,
                      "percent":(page_visit * 100.00) / total_visit,
                      "total_visit":total_visit
                      })