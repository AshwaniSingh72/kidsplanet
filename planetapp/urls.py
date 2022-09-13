from django.urls import path,include
from .import views
urlpatterns = [
  
    path("",views.home,name="home"),
    path("contactus/",views.contactus,name="contactus"),
    path("feedback/",views.feedback,name="feedback"),
    path("login/",views.login,name="login"),
    path("registration/",views.registration,name="registration"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path("edit_profile/",views.edit_profile,name="edit_profile"),
    path("admission/",views.admission,name="admission"),
    path("parent_logout/",views.parent_logout,name="parent_logout"),
    path("facilities/",views.facilities,name="facilities"),
    path("program_detail/",views.program_detail,name="program_detail"),
    path("job_detail/",views.job_detail,name="job_detail"),
]