from django.contrib import admin

from .models import Customer, Tickets

admin.site.site_header = "Portal Admin Clinique de la Paix 😎"
admin.site.site_title = "Portal Admin Clinique de la Paix 😎"
admin.site.index_title = "Welcome to Admin Sene Doctor"
# Register your models here.

@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ('type', 'patient', 'montant','create_at','update_at')
    search_fields = ('type',)
    def has_add_permission(self, request):
        return True

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    #list_display = ('type', 'patient', 'montant','create_at','update_at')
    def has_add_permission(self, request):
        return True

