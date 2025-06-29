from django.urls import path
from student import views

urlpatterns = [
    path('',views.student_list),
    path('<int:pk>/delete',views.student_delete_list),
    path('<int:pk>/update',views.student_update_list),
]