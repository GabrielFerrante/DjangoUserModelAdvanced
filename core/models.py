from django.db import models

#USANDO O USER MODEL PADRÃO DO DJANGO
#from django.contrib.auth.models import User

'''class Post(models.Model):
    autor = models.ForeignKey(User, verbose_name='autor', on_delete=models.CASCADE)
    titulo = models.CharField('Titulo', max_length=100)
    texto = models.CharField('Texto', max_length=100)

    def __str__(self):
        return self.titulo'''

#USANDO O USER MODEL PERSONALIZADO
'''from django.conf import settings

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='autor', on_delete=models.CASCADE)
    titulo = models.CharField('Titulo', max_length=100)
    texto = models.CharField('Texto', max_length=100)

    def __str__(self):
        return self.titulo'''

#USANDO O get_user_model ATUAL
#SE TIVER ESPECIFICA NO SETTINGS.PY, VAI AQUELE, SE NÃO, É PEGO O PADRÃO
from django.contrib.auth import get_user_model

class Post(models.Model):
    autor = models.ForeignKey(get_user_model(), verbose_name='autor', on_delete=models.CASCADE)
    titulo = models.CharField('Titulo', max_length=100)
    texto = models.CharField('Texto', max_length=100)

    def __str__(self):
        return self.titulo



