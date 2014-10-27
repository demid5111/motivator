from django.conf.urls import patterns, include, url

from aimer import views

urlpatterns = patterns('views',
    url(r'^$', views.index, name ='index'),
    url(r'^add', views.addNewAim, name ='addNewAim'),
    url(r'^aims', views.viewAims, name = 'viewAims'),
    url(r'^save_new_aim', views.saveNewAim, name="saveNewAim"),
)