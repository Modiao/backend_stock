from django.contrib import admin

from .models import Patient, Ticket

admin.site.site_header = "Portal Admin Clinique de la Paix 😎"
admin.site.site_title = "Portal Admin Clinique de la Paix 😎"
admin.site.index_title = "Welcome to Admin Sene Doctor"
# Register your models here.

@admin.register(Ticket)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ('id_ticket', 'type', 'patient', 'montant','create_at','update_at','is_valid')
    search_fields = ('id_ticket','is_valid')
    list_filter = ('type','is_valid' )
    def has_add_permission(self, request):
        return True

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'telephone','email','address', 'create_at','update_at')
    #search_fields =  ('telephone')
    def has_add_permission(self, request):
        return True

