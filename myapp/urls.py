from django.urls import path
from . import views
from django.conf import settings #add this
from django.conf.urls.static import static #add this



urlpatterns = [
     

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('upimage/', views.addProduct, name="add-product"), 
     
    path('consult/', views.consult, name='consult'),
    path('diagnosis/', views.diagnosis, name='diagnosis'),
    path('faq/', views.faq, name='faq'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('diagnosisInfo/', views.diagnosisInfo, name='diagnosisInfo'),
    path('user/', views.user, name='user'),
    path('uploadfaq/', views.uploadFaq, name="uploadfaq"),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

