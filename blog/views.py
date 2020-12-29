from django.utils import timezone
import markdown
import pysnooper
from django.shortcuts import render
from django.views.generic import DetailView,ListView

from .models import Artical

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
        artical=context["object"]
        filePath = context["object"].text

        re_context={}

        with open(filePath, "r", encoding="utf-8") as target:
            html = markdown.markdown(target.read(), extensions=['tables'])
            re_context["text"] = html

        re_context["title"]=artical.title
        re_context["postData"]=artical.postData
        re_context["readCount"]=artical.readCount

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
    
