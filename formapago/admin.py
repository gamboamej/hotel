from django.contrib import admin
from .models import *

class i001t_tipo_forma_pagoAdmin(admin.ModelAdmin):
    list_display        = ('co_tipo_forma_pago','tx_nombre','nu_orden','tx_enlace','in_activo')
    list_display_links  = ('tx_nombre','in_activo')
    search_fields       = ('co_tipo_forma_pago','tx_nombre',)
    list_editable       = ['nu_orden']
 #   date_hierarchy      = 'fe_crea'
    prepopulated_fields = {'tx_enlace' : ('tx_nombre',)}
    list_filter = ['in_activo']

class i002t_forma_pagoAdmin(admin.ModelAdmin):
    list_display        = ('co_forma_pago','tx_nombre','co_tipo','tx_foto','nu_orden','tx_enlace','in_activo')
    list_display_links  = ('tx_nombre','co_tipo','in_activo')
    search_fields       = ('co_forma_pago','tx_nombre',)
    list_editable       = ['nu_orden']
 #   date_hierarchy      = 'fe_crea'
    prepopulated_fields = {'tx_enlace' : ('tx_nombre',)}
    list_filter = ['in_activo']

admin.site.register(i001t_tipo_forma_pago,i001t_tipo_forma_pagoAdmin)
admin.site.register(i002t_forma_pago,i002t_forma_pagoAdmin)
