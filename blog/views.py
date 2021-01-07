import markdown
import pysnooper
from django.db.models.fields.files import FieldFile
from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import DetailView, ListView

from blog.forms import ArticalForm, ImageForm, LoginForm

from .models import Artical, Image

# Create your views here.


class ArticalDetailView(DetailView):
    model = Artical
    template_name = "blog/blog_detail.html"

    context_object_name = "artical_data"

    def get_queryset(self):
        return Artical.objects.all()

    @pysnooper.snoop()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artical = context["object"]
        filePath:FieldFile = context["object"].text

        re_context = {}

        #filePath.encoding="utf-8"
        html = markdown.markdown(filePath.read().decode("utf-8"), extensions=['tables'])
        re_context["text"] = html

        re_context["title"] = artical.title
        re_context["postData"] = artical.postData
        re_context["readCount"] = artical.readCount

        return re_context


class ArticalListView(ListView):
    model = Artical
    template_name = "blog/blog_list.html"

    def get_queryset(self):
        return Artical.objects.all

    @pysnooper.snoop()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class ImageListView(ListView):
    model = Image
    template_name = "blog/image_list.html"

    def get_queryset(self):
        return Image.objects.all
    



def login(request: HttpRequest):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/blog/")
    else:
        form = LoginForm()

    return render(request, "blog/login.html", {"form": form})


@pysnooper.snoop()
def upload_artical(request: HttpRequest):
    if request.method == "POST":
        form = ArticalForm(request.POST, request.FILES)

        if form.is_valid():
            # print(request.FILES["file"].read())
            form.save()

            return HttpResponseRedirect("/blog/")

    else:
        form = ArticalForm()

    return render(request, "blog/upload_file.html", {"form": form})

@pysnooper.snoop()
def image_uploader(r: HttpRequest):
    if r.method == "POST":
        form = ImageForm(r.POST, r.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/blog/imgs")

    else:
        form = ImageForm()

    return render(r, "blog/upload_img.html", {"form": form})
