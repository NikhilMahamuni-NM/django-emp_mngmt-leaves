from django.urls import path
from . import views


app_name = 'leave'

urlpatterns = [
    path('', views.home, name='home'),
    path('emp-register/', views.emp_register, name='emp-register'),
    path('mngr-register/', views.mngr_register, name='mngr-register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('emp/', views.emp_home, name='emp_home'),
    path('my-leaves/', views.leaves, name="leaves"),
    path('mngr/', views.mngr_home, name='mngr_home'),
    path('apply-for-leave/', views.leave_apply, name='leave_apply'),
    path('leaveapprovals/', views.leave_approval, name='leave_approval'),
    path('leaveapprovals/<id>', views.leave_detail, name='leave_detail'),
    path('leaveapprovals/dismiss/<id>', views.dismiss, name='dismiss'),
    path('leaveapprovals/disapprove/<id>', views.disapprove, name='disapprove'),
    path('my-leaves/withdraw/<id>', views.withdraw, name='withdraw'),
]