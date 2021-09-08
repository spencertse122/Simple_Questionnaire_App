from django.http import HttpResponse
from django.views import generic 
from django.apps import apps
from django.shortcuts import render
from django.template import loader 

# class HomeView(generic.DetailView):
#     template_name = 'home/index.html'
#     context_object_name = 'list_of_apps'

#     def get_queryset(self):
#         return "This is homepage"

def HomeView(request):
    list_of_apps = apps.get_app_configs()
    context = {'list_of_apps': list_of_apps}
    template = loader.get_template('home/home.html')
    return HttpResponse(template.render(context, request))

app_models = apps.get_models()

# class HomeView(generic.ListView):
#     template_name = 'home/home.html'
#     context_object_name = 'list_of_apps'

#     # def get_queryset(self):
#     #     return 