from django.contrib import admin

from planetapp.models import AdmissionForm, City_event, Contact, Feedback, JobDescription, Parent_detail, Program_detail,Event

# Register your models here.

class Admin_Contact(admin.ModelAdmin):
    list_display=('name','email','phone','question')  ### it will show data in tabular format.
    search_fields=('name',)


class Admin_Parent(admin.ModelAdmin):
    list_display=('id','phone','email')  ### it will show data in tabular format.
    search_fields=('id',)

class Admin_Feedback(admin.ModelAdmin):
    list_display=('feedback_id','name','email','programe_name')  ### it will show data in tabular format.
    search_fields=('name','programe_name')

class Admin_Job(admin.ModelAdmin):
    list_display=('job_id','post_name','no_of_seat','last_apply')  ### it will show data in tabular format.
    search_fields=('job_id','post_name')

class Admin_Event(admin.ModelAdmin):
    list_display=('event_id','event_name','city','address')  ### it will show data in tabular format.
    search_fields=('event_id','address')

class Admin_Program(admin.ModelAdmin):
    list_display=('program_name','duration','fees','start_date','end_date')  ### it will show data in tabular format.
    search_fields=('program_name','city')

class Admin_Admission(admin.ModelAdmin):
    list_display=('program_name','kid_name','kid_age','father_name','phone','address')  ### it will show data in tabular format.
    search_fields=('program_name','kid_name')


admin.site.register(Contact,Admin_Contact)
admin.site.register(Feedback,Admin_Feedback)
admin.site.register(Parent_detail,Admin_Parent)
admin.site.register(JobDescription,Admin_Job)
admin.site.register(City_event)
admin.site.register(Program_detail,Admin_Program)
admin.site.register(AdmissionForm,Admin_Admission)
admin.site.register(Event,Admin_Event)

admin.site.site_header="Kids Planet Administarations"
admin.site.site_title="Kids Admin Dashboard"
admin.site.index_title="Welcome to Our Portal"