from blog.views import ArticalDetailView, ArticalListView
from django.urls import path
app_name="blog"
urlpatterns = [
    path(r"<int:pk>/",ArticalDetailView.as_view() , name="blog_page"),
    path("", ArticalListView.as_view(), name="blog_index")
]
