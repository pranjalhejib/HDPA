#LungsApp/urls.py created manually
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from LungsApp import views
urlpatterns = [
    path('', views.lungs, name='lungs'),
]
# # add the following line at the end of the file
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)