from django.db import models
from django.contrib.auth.models import User

class Cuenta(models.Model):
    """ Cuenta base que contiene subcuentas """

    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    saldo_real = models.DecimalField(default=0, max_digits=10, decimal_places=2)
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