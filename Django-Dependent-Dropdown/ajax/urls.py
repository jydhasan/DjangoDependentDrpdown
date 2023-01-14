from django.urls import path

from ajax.views import home, loadsubcat

urlpatterns = [
    path('',home,name="home"),
    path('load-subcat/',loadsubcat,name="load_subcat")
]
