from django.views.generic import ListView
from .models import video
class sos(ListView):
	model = video
	template_name = 'home.html'
	context_object_name='app1'