from django.shortcuts import render,redirect
from blog.forms import YaziEkleModelForm
from django.contrib.auth.decorators import login_required

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
