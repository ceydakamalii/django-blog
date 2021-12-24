from django.shortcuts import redirect, get_object_or_404
from blog.models import YazilarModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def yazi_sil(request, slug):
    get_object_or_404(YazilarModel, slug=slug, yazar=request.user).delete()
    return redirect('yazilarim')
