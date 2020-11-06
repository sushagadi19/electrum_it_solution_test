from django.conf.urls import url
from .views import MoviesView

urlpatterns = [
    url('movies', MoviesView.as_view(), name="MoviesView"),

]
