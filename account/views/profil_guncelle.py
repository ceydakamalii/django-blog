from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import ProfilDuzenlemeForm
@login_required(login_url='/')
def profil_guncelle(request):
    if request.method== 'POST':
        form= ProfilDuzenlemeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profil Güncellendi.')
    else:
       form= ProfilDuzenlemeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'pages/profil-guncelle.html', context=context)