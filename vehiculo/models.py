from django.db import models


class Vehiculo(models.Model):
    MARCAS = [
    ('Ford',"Ford"),
    ('Toyota', "Toyota"),
    ('Fiat',"Fiat"),
    ('Chevrolet',"Chevrolet")
    ]

    marca = models.CharField(max_length=20, 
                choices=MARCAS,default='ford')
    
    modelo = models.CharField(max_length=100)

    serial_carroceria = models.CharField(max_length=50)

    serial_motor = models.CharField(max_length=50)

    CATEGORIAS = [
        ("Particular","Particular"),
        ("Transporte", 'Transporte'),
        ("Carga",'Carga')
    ]

    categoria = models.CharField(max_length=20,
                choices=CATEGORIAS,default='Particular')
    
    precio = models.FloatField()
    
    fecha_de_creacion = models.DateField(auto_now_add=True)
    
    fecha_de_modificacion = models.DateField(auto_now=True)