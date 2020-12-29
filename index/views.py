
from django.shortcuts import render
import markdown
import pysnooper
# Create your views here.
@pysnooper.snoop()
def markDownView(request):
    with open("D:\project\personalBlog\ReadMe.md",encoding="UTF-8") as target:
        context=target.read()
        context=markdown.markdown(context,extensions=["tables"])
    return render(request,"index/MDabout.html",{"context":context})