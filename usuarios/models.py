from django.db import models

# Create your models here.


class Usuario(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True, blank=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    tipoUsuario = models.CharField(max_length=50)
    idautenticacion = models.ForeignKey('Autenticaciones', on_delete=models.CASCADE)


class Autenticaciones(models.Model):
    idautenticacion = models.BigAutoField(primary_key=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)


class Rating(models.Model):
    idrating = models.BigAutoField(primary_key=True, blank=True)
    calificaciones = models.CharField(max_length=100)
    cedula = models.ForeignKey('Usuario', on_delete=models.CASCADE)


class Aprobaciones(models.Model):
    idaprobaciones = models.BigAutoField(primary_key=True, blank=True)
    nombreusuario = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    copiaCedula = models.CharField(max_length=50)
    certificadoLibertad = models.CharField(max_length=50)
    idinmueble = models.ForeignKey('Inmuebles', on_delete=models.CASCADE, null=True)
    cedula = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True)


class Inmuebles(models.Model):
    idinmueble = models.BigAutoField(primary_key=True, blank=True)
    nombre = models.CharField(max_length=20)
    tipoInmueble = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=150)
    precio = models.FloatField(max_length=30)
    direccion = models.CharField(max_length=50)
    imagen = models.CharField(max_length=50)
    cedula = models.ForeignKey('Usuario', on_delete=models.CASCADE)


class Citas(models.Model):
    idcita = models.BigAutoField(primary_key=True, blank=True)
    horaCita = models.DateTimeField()
    usuarios = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='UsuarioFk')
    asesor = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='AsesorFk')

