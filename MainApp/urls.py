#MainApp/urls.py created manually
from django.conf.urls.static import static
from django.conf import settings

from django.urls import include, path
from MainApp import views
urlpatterns = [
    path("", views.index, name='index'),
    path("services/",views.services, name='services'),
    path("about/",views.about, name='about'),
    path("contact/",views.contact, name='contact'),

]
# # add the following line at the end of the file
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL_MAINAPP, document_root=settings.MEDIA_ROOT_MAINAPP)