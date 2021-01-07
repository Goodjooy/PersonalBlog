from django.http.response import HttpResponseRedirect
from blog.views import ArticalDetailView, ArticalListView, ImageListView, login, upload_artical, image_uploader
from django.urls import path
app_name="blog"
urlpatterns = [
    path("upload/",lambda x:HttpResponseRedirect("/blog/upload/md")),
    path("upload/img",image_uploader,name="img_up"),
    path("upload/md",upload_artical,name="upload"),
    path("login/",login,name="login"),
    path(r"<int:pk>/",ArticalDetailView.as_view() , name="blog_page"),
    path("", ArticalListView.as_view(), name="blog_index"),
    path("imgs/", ImageListView.as_view(), name="image_list"),
]
