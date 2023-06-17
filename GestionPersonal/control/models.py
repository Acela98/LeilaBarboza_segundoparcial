from django.db import models

# Create your models here.
class Empleado(models.Model):

    idempledo=models.IntegerField
    nombre=models.CharField(max_length=200)
    departamento=models.CharField(max_length=200)
    fecha_de_inicio=models.DateField
    dias_trabajo=models.CharField(max_length=200)
    turno=models.CharField(max_length=15)
    horario_entrada=models.CharField(max_length=15)
    horario_salida=models.CharField(max_length=15)

    

    def __str__(self):
        return self.nombre
    

class Jornada(models.Model):

    idjornada=models.IntegerField
    fecha=models.DateField
    tipo_marcacion=models.IntegerField
    idempleado=models.ForeignKey(Empleado, on_delete=models.CASCADE)


    def __str__(self):
        return self.fecha 


