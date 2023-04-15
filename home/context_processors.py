from .models import AmigoModels, SolisitudMOdel, PostModel
from django.contrib.auth.decorators import login_required
from django.db.models  import Sum, Count
def validar_amigo(usuario, user):
    if AmigoModels.objects.filter(user=user, añadidos=usuario).exists():
        return True
    else:
        return False 
    


def amigos_context(request):
    
    if request.user.is_authenticated:
  
        cantidad = SolisitudMOdel.objects.filter(solisitud=request.user).count()
        amigos = AmigoModels.objects.filter(user=request.user).count()
        like = PostModel.objects.filter(user=request.user).values('like_post_reverse__id').annotate(cantid = Count('like_post_reverse__id')) 
        lista = list()
        [lista.append(numero['cantid']) for numero in like  ]
        post = PostModel.objects.filter(user=request.user).count()
        return {
            'cantidad':cantidad,
            'totalamigos':amigos,
            'post':post,
            'like':sum(lista),
            'variable':None,
            
        }
    else:
          return {
            
        }