from django.urls import path
from main.views import (
    show_main,
    show_education,
    show_projects,
    show_project_json,
    show_experience,
    show_experience_json,
    create_experience,
    update_experience,
    delete_experience,
    create_project,
    create_project_ajax,
    update_project,
    delete_project,
    toggle_star,
    register,
    login_user,
    logout_user,
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('education/', show_education, name='show_education'),
    path('projects/', show_projects, name='show_projects'),
    path('projects/json/', show_project_json, name='show_project_json'),
    path('projects/create/', create_project, name='create_project'),
    path('projects/create-ajax/', create_project_ajax, name='create_project_ajax'),
    path('projects/update/<uuid:id>/', update_project, name='update_project'),
    path('projects/delete/<uuid:id>/', delete_project, name='delete_project'),
    path('toggle-star/<uuid:id>/', toggle_star, name='toggle_star'),
    path('experience/', show_experience, name='show_experience'),
    path('experience/json/', show_experience_json, name='show_experience_json'),
    path('experience/create/', create_experience, name='create_experience'),
    path('experience/update/<uuid:id>/', update_experience, name='update_experience'),
    path('experience/delete/<uuid:id>/', delete_experience, name='delete_experience'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]