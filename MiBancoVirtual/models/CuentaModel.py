from django.db import models
from django.contrib.auth.models import User

class Cuenta(models.Model):
    """ Cuenta base que contiene subcuentas """

    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    es_efectivo = models.BooleanField(default=False)
    b_Q100 = models.IntegerField(default=0)
    b_Q50 = models.IntegerField(default=0)
    b_Q20 = models.IntegerField(default=0)
    b_Q10 = models.IntegerField(default=0)
    b_Q5 = models.IntegerField(default=0)
    m_100c = models.IntegerField(default=0)
    m_50c = models.IntegerField(default=0)
    m_25c = models.IntegerField(default=0)
    m_10c = models.IntegerField(default=0)
    m_5c = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
        
    def calcular_efectivo(self):
        self.total = 0

        self.total += self.b_Q100 * 100
        self.total += self.b_Q50 * 50
        self.total += self.b_Q20 * 20
        self.total += self.b_Q10 * 10
        self.total += self.b_Q5 * 5
        self.total += self.m_100c
        self.total += self.m_50c * 50 / 100
        self.total += self.m_25c * 25 / 100
        self.total += self.m_10c * 10 / 100
        self.total += self.m_5c * 5 / 100

        return self.total