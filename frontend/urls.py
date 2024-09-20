from django.urls import path
from frontend import views

urlpatterns = [
    #===========================================================================================
    path('home/', views.frontindex, name='frontindex'),
    path('services/', views.services, name='services'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
    path('send_contact_message/', views.send_contact_message, name='send_contact_message'),
    #===========================================================================================
    path('view_all/', views.view_all, name='view_all'),
    path('see_details/<stadium_name>/', views.see_details, name='see_details'),
    #===========================================================================================
    path('apply_agent/', views.apply_agent, name='apply_agent'),
    path('save_applied_agent/', views.save_applied_agent, name='save_applied_agent'),
    path('agent_details/<agent_name>/', views.agent_details, name='agent_details'),
    #===========================================================================================
    path('frequently-asked-questions/', views.faq, name='faq'),
    path('our_terms/', views.our_terms, name='our_terms'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('our_partners/', views.our_partners, name='our_partners'),
    #===========================================================================================
    path('careers/', views.careers, name='careers'),
    path('careers_filtered/<career_name>/', views.careers_filtered, name='careers_filtered'),
    path('save_careers_filtered/', views.save_careers_filtered, name='save_careers_filtered'),
    #===========================================================================================
    path('payment_redirect/<stadium_name>/', views.payment_redirect, name='payment_redirect'),
    path('payment_success/<stadium_name>/', views.payment_success, name='payment_success'),

]