from django.shortcuts import render


def anasayfa(request):
    context = {
        'isim': 'Ceyda kamali'
    }
    return render(request, 'pages/anasayfa.html', context=context)