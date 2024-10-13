from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    return about_view(request)


def about_view(request, *args, **kwargs):
    my_title = "My Page"
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() * 100) / qs.count()
    except:
        percent = 0    
    html_template = "home.html" 
    my_context = {
        "page_title": my_title,
        "page_visits_count": page_qs.count(),
        "percent": percent,
        "total_visits_count": qs.count()
    }
    path = request.path
    print("path", request.path)    
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)


def my_old_home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title": my_title
    }
    html_ = """
    <!DOCTYPE html>

    <html>

    <body>
        <h1>This is anything</h1>
    </body>
    </html>
    """.format(**my_context)
    html_file_path = this_dir / "home.html"
    html_ = html_file_path.read_text()
    return HttpResponse(html_)