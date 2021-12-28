from django.forms import fields
from django.shortcuts import render,redirect
from blog.forms import YaziEkleModelForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from blog.models import YazilarModel
from django.contrib.auth.mixins import LoginRequiredMixin


class YaziEkleCreateView(LoginRequiredMixin, CreateView):
    login_url =reverse_lazy('giris')
    template_name='pages/yazi-ekle.html'
    model = YazilarModel
    fields = ('baslik', 'icerik', 'resim', 'kategoriler')

    def form_valid(self, form):
        yazi = form.save(commit=False) #db ye kaydetmiyor yer açıyor
        yazi.yazar = self.request.user
        yazi.save()
        form.save_m2m() #many to many ilişkisiyle ilişkilendirilen kategorileride dbye kaydetmek için yapıyoruz
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detay', kwargs={
            'slug': self.object.slug
        })

@login_required(login_url='/')
def yazi_ekle(request):

    form= YaziEkleModelForm(request.POST or None, files=request.FILES or None)
    ## istek varsa request.POST'u ver yoksa None ver, data geldiyse files o data olsun gelmediyse none olsun.
    if form.is_valid():
        yazi = form.save(commit=False) #db ye kaydetmiyor yer açıyor
        yazi.yazar = request.user
        yazi.save()
        form.save_m2m() #many to many ilişkisiyle ilişkilendirilen kategorileride dbye kaydetmek için yapıyoruz
        return redirect('detay', slug=yazi.slug)
    context = {
        'form': form
    }

    return render(request, 'pages/yazi-ekle.html', context=context)
