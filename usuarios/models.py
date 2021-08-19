from django.db import models

# Create your models here.

from django.contrib.auth.models import (AbstractBaseUser
, AbstractUser, BaseUserManager)

#Gerenciador de criação de usuários
class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    #Arruma os dados e retorna o usuário
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    #Especifica o create user para usuários comuns
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    #Especifica o create user para usuários staff e super
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter o atributo ativado')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter o atributo ativado')

        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    cpf = models.CharField('CPF', max_length=14)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone', 'cpf']

    objects = UsuarioManager()

    def __str__(self):
        return self.email

    

'''class CustomUsuario(AbstractBaseUser):
    pass

    def __str__(self):
        return self.email'''
