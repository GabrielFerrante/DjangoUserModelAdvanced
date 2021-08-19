from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import CustomUsuario


class CustomUsuarioCreationForm(UserCreationForm):
    class meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone', 'cpf')
        labels = {'username' : 'Username/E-mail'}

    
    #Save custom
    def save(self, commit=True):
        #Não salva de primeira, vamos manipular o usuário
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        
        if commit is True:
            user.save()

        return user


class CustomUsuarioChangeForm(UserChangeForm):
    class meta:
        model = CustomUsuario
        fields = ['first_name', 'last_name', 'fone', 'cpf']
