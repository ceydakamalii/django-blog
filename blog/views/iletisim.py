from django.shortcuts import render, redirect
from blog.forms import IletisimForm
from blog.models import IletisimModel
from django.views.generic import FormView


class IletisimFormView(FormView):
    template_name='pages/iletisim.html'
    form_class = IletisimForm
    success_url='/email-gonderildi'

    def form_valid(self,form):
        form.save()
        form.send_email(mesaj=form.cleaned_data.get('mesaj'))
        return super().form_valid(form)

def iletisim(request):
    form = IletisimForm()
    if request.method =="POST":
        #print(request.POST)
        form = IletisimForm(request.POST)
        if form.is_valid():
            #form.cleaned_data.get('email')
            #form kullanara
            ##iletisim = IletisimModel()
            ##iletisim.email = form.cleaned_data['email']
            ##iletisim.isim_soyisim = form.cleaned_data['isim_soyisim']
            ##iletisim.mesaj = form.cleaned_data['mesaj']
            ##iletisim.save()

            #Modelform kullanarak
            form.save()
            return redirect('anasayfa')

    context = {
        'form': form
    
    }
    return render(request, 'pages/iletisim.html', context=context)