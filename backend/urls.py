from django.urls import path
from backend import views

urlpatterns = [
    # =========================== HOME-PAGE ==========================================================
    path('admin/', views.backindex, name='backindex'),
    
    # =========================== GROUND =============================================================
    path('add-ground/', views.add_ground, name='add_ground'),
    path('save_ground/', views.save_ground, name='save_ground'),
    path('view_ground/', views.view_ground, name='view_ground'),
    path('edit_ground/<int:ground_id>/', views.edit_ground, name='edit_ground'),
    path('update_ground/<int:ground_id>/', views.update_ground, name='update_ground'),
    path('remove_ground/<int:ground_id>/', views.remove_ground, name='remove_ground'),
    path('remove_all_ground/', views.remove_all_ground, name='remove_all_ground'),
    
    # =========================== FEEDBACK ===========================================================
    path('view_feedback/', views.view_feedback, name='view_feedback'),
    path('delete_all_feedback/', views.delete_all_feedback, name='delete_all_feedback'),
    path('delete_feedback/<int:feed_id>/', views.delete_feedback, name='delete_feedback'),

    # =========================== TESTIMONIAL ========================================================
    path('add_testimonial/', views.add_testimonial, name='add_testimonial'),
    path('add_as_testimonial/<int:feed_id>/', views.add_as_testimonial, name='add_as_testimonial'),
    path('save_testimonial/', views.save_testimonial, name='save_testimonial'),
    path('view_testimonial/', views.view_testimonial, name='view_testimonial'),
    path('delete_all_testimonial/', views.delete_all_testimonial, name='delete_all_testimonial'),
    path('delete_testimonial/<int:feed_id>/', views.delete_testimonial, name='delete_testimonial'),
    
    # =========================== AGENTS =============================================================
    path('add_agents/', views.add_agents, name='add_agents'),
    path('save_agents/', views.save_agents, name='save_agents'), 
    path('view_agents/', views.view_agents, name='view_agents'), 
    path('edit_agents/<int:agent_id>/', views.edit_agents, name='edit_agents'), 
    path('update_agents/<int:agent_id>/', views.update_agents, name='update_agents'), 
    path('remove_agents/<int:agent_id>/', views.remove_agents, name='remove_agents'), 
    path('remove_all_agents/', views.remove_all_agents, name='remove_all_agents'),
    
    # =========================== CAREERS ============================================================
    path('add_careers/', views.add_careers, name='add_careers'),
    path('save_careers/', views.save_careers, name='save_careers'),
    path('view_careers/', views.view_careers, name='view_careers'),
    path('edit_careers/<int:career_id>/', views.edit_careers, name='edit_careers'),
    path('update_careers/<int:career_id>/', views.update_careers, name='update_careers'),
    path('delete_careers/<int:career_id>/', views.delete_careers, name='delete_careers'),
    path('delete_all_careers/', views.delete_all_careers, name='delete_all_careers'),
    
    # =========================== CAREERS-REQUESTS ===================================================
    path('view_career_requests/', views.view_career_requests, name='view_career_requests'),
    path('delete_all_career_requests/', views.delete_all_career_requests, name='delete_all_career_requests'),
    
    # =========================== PARTNERS ===========================================================
    path('add_partners/', views.add_partners, name='add_partners'),
    path('save_partners/', views.save_partners, name='save_partners'),
    path('display_partners/', views.display_partners, name='display_partners'),
    path('delete_partners/<int:partner_id>/', views.delete_partners, name='delete_partners'),
    
    # =========================== FORM-ELEMENTS ======================================================
    path('admin_index/', views.admin_index, name='admin_index'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    
]