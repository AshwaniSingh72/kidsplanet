from django.contrib import admin

from planetapp.models import AdmissionForm, City_event, Contact, Feedback, JobDescription, Parent_detail, Program_detail,Event

# Register your models here.

class Admin_Contact(admin.ModelAdmin):
    list_display=('name','email','phone','question')  ### it will show data in tabular format.
    search_fields=('name',)


class Admin_Parent(admin.ModelAdmin):
    list_display=('id','phone','email')  ### it will show data in tabular format.
    search_fields=('id',)
admin.site.register(Contact,Admin_Contact)
admin.site.register(Feedback)
admin.site.register(Parent_detail,Admin_Parent)
admin.site.register(JobDescription)
admin.site.register(City_event)
admin.site.register(Program_detail)
admin.site.register(AdmissionForm)
admin.site.register(Event)

admin.site.site_header="Kids Planet Administarations"
admin.site.site_title="Kids Admin Dashboard"
admin.site.index_title="Welcome to Our Portal"