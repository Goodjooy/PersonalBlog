from index.views import markDownView
from django.conf.urls import url


urlpatterns = [
    url("about/",markDownView),
]
