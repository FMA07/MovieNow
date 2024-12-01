from django.contrib.admin import AdminSite
from appClientes.models import Usuario, Cliente, Reserva
from appVendedor.models import Vendedor
from pagWeb.models import Catalogo, Pelicula

class MyAdminSite(AdminSite):
    site_header = "Unified Admin"
    site_title = "My Project Admin"
    index_title = "Welcome to the Unified Admin"

admin_site = MyAdminSite(name="custom_admin")

# Register models from all apps
admin_site.register(Usuario)
admin_site.register(Cliente)
admin_site.register(Reserva)
admin_site.register(Vendedor)
admin_site.register(Catalogo)
admin_site.register(Pelicula)

