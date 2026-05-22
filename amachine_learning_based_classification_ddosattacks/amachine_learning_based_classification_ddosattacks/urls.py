"""
AMachine_Learning_Based_Classification_DDoSAttacks URL Configuration
"""

from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

# App views
from Remote_User import views as remoteuser
from Service_Provider import views as serviceprovider
from Remote_User.views import quantum_view


urlpatterns = [

    # ================== QUANTUM COMPUTING ==================
    path('quantum/', quantum_view, name='quantum'),

    # ================== ADMIN ==================
    path('admin/', admin.site.urls),

    # ================== REMOTE USER ==================
    re_path(r'^$', remoteuser.login, name="login"),
    re_path(r'^Register1/$', remoteuser.Register1, name="Register1"),
    re_path(r'^predict_ddos_attack_type/$', remoteuser.predict_ddos_attack_type, name="predict_ddos_attack_type"),
    re_path(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    re_path(r'^logout/$', remoteuser.logout_view, name='logout'),

    # ================== SERVICE PROVIDER ==================
    re_path(r'^serviceproviderlogin/$', serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    re_path(r'^View_Remote_Users/$', serviceprovider.View_Remote_Users, name="View_Remote_Users"),

    re_path(r'^charts/(?P<chart_type>\w+)$', serviceprovider.charts, name="charts"),
    re_path(r'^charts1/(?P<chart_type>\w+)$', serviceprovider.charts1, name="charts1"),
    re_path(r'^likeschart/(?P<like_chart>\w+)$', serviceprovider.likeschart, name="likeschart"),

    re_path(
        r'^Find_View_Prediction_DDOS_Attack_Type_Ratio/$',
        serviceprovider.Find_View_Prediction_DDOS_Attack_Type_Ratio,
        name="Find_View_Prediction_DDOS_Attack_Type_Ratio"
    ),

    re_path(
        r'^Train_Test_DataSets/$',
        serviceprovider.Train_Test_DataSets,
        name="Train_Test_DataSets"
    ),

    re_path(
        r'^View_Prediction_DDOS_Attack_Type/$',
        serviceprovider.View_Prediction_DDOS_Attack_Type,
        name="View_Prediction_DDOS_Attack_Type"
    ),

    re_path(
        r'^Download_Trained_DataSets/$',
        serviceprovider.Download_Trained_DataSets,
        name="Download_Trained_DataSets"
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
