from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor')
    #Excluindo o campo autor do formulario
    exclude = ['autor', ]

    #Para aparecer o nome full
    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'

    
    #Filtrando os dados do autor logado
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)

    #Devido a falta do campo autor, salva o Post com o autor sendo o usuário da requisição
    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)