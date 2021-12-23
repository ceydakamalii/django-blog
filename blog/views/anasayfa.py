from django.core import paginator
from django.shortcuts import render
from blog.models import YazilarModel
from django.core.paginator import Paginator
from django.db.models import Q

def anasayfa(request):
    yazilar = YazilarModel.objects.order_by('-id')
    sorgu= request.GET.get('sorgu')
    if sorgu:
        yazilar = yazilar.filter(
            Q(baslik__icontains=sorgu) |
            Q(icerik__icontains=sorgu)
        )

    sayfa= request.GET.get('sayfa')
    paginator = Paginator(yazilar, 2) # bir sayfada 2 tane yazı olucak
    context = {
        'yazilar': paginator.get_page(sayfa)
    }
    return render(request, 'pages/anasayfa.html', context=context)