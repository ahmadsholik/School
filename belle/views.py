from django.views import View
from django.views.generic.list import ListView
from django.shortcuts import render

from .models import *


class Home(View):

    template_name = "belle/homepage.html"

    def get(self, request):
        return render(request, template_name=self.template_name)


class ThisWeek(ListView):

    template_name = "belle/This_Week.html"
    queryset = Week.objects.latest("pk").song_set.all()
    context_object_name = "songs"


class ColorScheme(View):

    template_name = "belle/Color_Scheme.html"
    context = {
        "colors": ["fff66a", "ffe200", "ffc900", "502f00", "412000"]
    }

    def get(self, request):
        return render(request, template_name=self.template_name, context=self.context)
