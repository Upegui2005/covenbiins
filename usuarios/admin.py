from django.contrib import admin

from usuarios.models import Usuario, Autenticaciones, Rating, Aprobaciones, Inmuebles, Citas


# Register your models here.


class UsuarioAdmin(admin.ModelAdmin):
    fields = ["cedula", "nombre", "apellido", "fechaNacimiento", "telefono", "direccion", "tipoUsuario",
              "idautenticacion"]
    list_display = ["cedula", "nombre", "apellido", "fechaNacimiento", "telefono", "direccion", "tipoUsuario",
                    "idautenticacion"]


class AutenticacionesAdmin(admin.ModelAdmin):
    fields = ["email", "password"]
    list_display = ["idautenticacion", "email", "password"]


class RatingAdmin(admin.ModelAdmin):
    fields = ["calificaciones", "cedula"]
    list_display = ["idrating", "calificaciones", "cedula"]


class AprobacionesAdmin(admin.ModelAdmin):
    fields = ["nombreusuario", "direccion", "copiaCedula", "certificadoLibertad", "idinmueble", "cedula"]
    list_display = ["idaprobaciones", "nombreusuario", "direccion", "copiaCedula", "certificadoLibertad", "idinmueble", "cedula"]


class InmueblesAdmin(admin.ModelAdmin):
    fields = ["nombre", "tipoInmueble", "descripcion", "precio", "direccion", "imagen", "cedula"]
    list_display = ["idinmueble", "nombre", "tipoInmueble", "descripcion", "precio", "direccion", "cedula", "imagen"]


class CitasAdmin(admin.ModelAdmin):
    fields = ["horaCita", "usuarios", "asesor"]
    list_display = ["idcita", "horaCita", "usuarios", "asesor"]


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Autenticaciones, AutenticacionesAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Aprobaciones, AprobacionesAdmin)
admin.site.register(Inmuebles, InmueblesAdmin)
admin.site.register(Citas, CitasAdmin)