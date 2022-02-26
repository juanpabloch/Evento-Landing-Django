from django.shortcuts import render

# Create your views here.


def index(request):
    # form = RegistroForm()
    # if request.method == 'POST':
    #     form = RegistroForm(request.POST)
    #     if form.is_valid():
    #         form_data = form.cleaned_data
    #         send_email(form_data['email'], form_data['nombre'])
    #         form.save()
    #         form = RegistroForm()
    #         context = {
    #             'form': form,
    #             'active': 'active'
    #         }
    #         return render(request, 'EventoHumanizar/index.html', context)
    # context = {
    #     'form': form,
    #     'active': ''
    # }
    return render(request, 'evento/index.html')
