from django.urls import path
from .views import *


urlpatterns = [
	path('hello/', hello),
	path('sum/', summ),
	path('mail/', mail)
	]
