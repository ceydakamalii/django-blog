from django.shortcuts import redirect,render
from django.contrib import messages
from account.forms import KayitFormu
from django.contrib.auth import login, authenticate
def kayit(request):
    if request.method== 'POST':
        form=KayitFormu(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Üye Oldunuz.')
            return redirect('anasayfa')

    else:
       form=KayitFormu()
    context = {
        'form':form
    }
    return render(request, 'pages/kayit.html', context=context)