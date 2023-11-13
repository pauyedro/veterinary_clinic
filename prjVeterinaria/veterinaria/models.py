from django.db import models

# Create your models here.


TIPO_IVA_CHOICE = (
    ("CF", "Consumidor Final"),
    ("RI", "Responsable Inscripto"),
    ("MT", "Monotributo")
)


class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Localidad(models.Model):
    nombre = models.CharField(max_length=50)
    cp = models.CharField("Cod. Postal", max_length=10)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre + " - " + self.cp


class Tipo_Doc(models.Model):
    diminutivo = models.CharField(max_length=3, null=True, blank=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.diminutivo


class Cliente(models.Model):
    nombre = models.CharField("Nombre/s",max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(null=True, blank=True)
    tipo_doc = models.ForeignKey(Tipo_Doc, on_delete=models.PROTECT, null=True, blank=True)
    nro_doc = models.IntegerField("Nro de Doc.", null=True, blank=True)
    cuit = models.CharField("CUIT", max_length=16, null=True, blank=True)
    tipo_iva = models.CharField("Tipo de IVA", max_length=2, choices=TIPO_IVA_CHOICE, default="CF")
    activo = models.BooleanField(default=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    fecha_nac = models.DateField("Fecha de Nacimiento", null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Mascota(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    edad = models.IntegerField(null=True, blank=True)
    especie = models.CharField("Especie/Raza", max_length=50)
    historial = models.CharField(max_length=255)
    dueno = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.especie + "-" + self.nombre + "<br>" + self.historial



