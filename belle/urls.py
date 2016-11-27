from django.conf.urls import url
from .views import *

app_name = "belle"
urlpatterns = [
    url(r"^$", Home.as_view(), name="home"),
    url(r"^This_Week$", ThisWeek.as_view(), name="this_week"),
    url(r"^Color_Scheme$", ColorScheme.as_view(), name="color_scheme"),
]
