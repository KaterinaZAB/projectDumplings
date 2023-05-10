from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template

from restasite.forms import contact_form
from restasite.models import menu_item
# Create your views here.

def pelmeni(request, category=None):
    # menu_chi = menu_item.objects.filter(type__exact='CHI').order_by('?')[:6]
    # menu_bef = menu_item.objects.filter(type__exact='BEF').order_by('?')[:6]
    # menu_veg = menu_item.objects.filter(type__exact='VEG').order_by('?')[:6]

    menu = menu_item.objects.all().order_by('type')

    if category:
        menu = menu_item.objects.filter(type__exact=category)

    print(menu)

    # словарь фильтров
    context = {
        # 'menu_chi': menu_chi,
        # 'menu_bef': menu_bef,
        # 'menu_veg': menu_veg,
        'menu': menu
    }
    return render(
        request,
        'pelmeni.html',
        context=context
    )

def pelmennaia(request):
    return render(
        request,
        'pelmennaia.html'
    )
def index(request):
    return render(
        request,
        'index.html'
    )
def contact(request):
    context={}
    if request.method=='POST':
        form = contact_form(request.POST)
        # проверка корректности полей формы
        if form.is_valid():
            send_message(
                form.cleaned_data['name'],
                form.cleaned_data['email'],
                form.cleaned_data['message']
            )
            context={'success': 1}
    else:
        form = contact_form()
    context['form'] = form
    return render(
        request,
        'contact.html',
        context=context
    )

def send_message(name,email,message):
    text=get_template('message.html')
    html=get_template('message.html')
    context = {
        'name':name, 'email':email,'message':message
    }
    #тема для письма
    subject='Сообщение от пользователя'
    from_email='from@example.com'
    text_content=text.render(context)
    html_content = text.render(context)

    msg=EmailMultiAlternatives(subject,text_content,from_email, ['manager@example.com'])
    # добавление альтернативной версии
    msg.attach_alternative(html_content,'text/html')
    msg.send()
