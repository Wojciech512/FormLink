from django.contrib import admin
from django.urls import path
from . import views as proxy_views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("",proxy_views.startPage,name="start-page"),
    path("login/", LoginView.as_view(template_name="proxymodelapp/login.html"), name="login-user"),
    path("logout/", LogoutView.as_view(template_name="proxymodelapp/logout.html"), name="logout-user"),
    path("doctor_registration/", proxy_views.doctor_registration, name="doctor-registration"),    
    path("patient_registration/", proxy_views.patient_registration, name="patient-registration"),
    path('newform/', proxy_views.new_form,name='newform'),
    path('list/',proxy_views.list_pdfs,name='list'),
    path('delete/<int:id>/',proxy_views.delete_form,name='deleteform'),
    path('view/<int:id>/',proxy_views.view_form,name='viewform'),
    path('<int:id>/',proxy_views.download_form,name='generateform'),
    path('admin/', proxy_views.login_admin, name='admin'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)