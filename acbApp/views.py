from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import FeedbackModel
from .forms import ContactForm
from django.views.decorators.cache import cache_control

# Create your views here.

cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    return render(request, 'acbApp/index.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        ContactForm(request.POST)
        if form.is_valid():
            print('form validation process successful....')
            print('name', form.cleaned_data['name'])
            print('email', form.cleaned_data['email'])
            print('phone', form.cleaned_data['phone'])
            print('address', form.cleaned_data['address'])
            print('message', form.cleaned_data['message'])
    return render(request, 'acbApp/contact.html', context={'form': form})

def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        messages = request.POST['message']
        formdata = FeedbackModel(name = name, email = email, phone = phone, address = address, message = messages)
        formdata.save()
        msg= 'Form Submitted...'
        form = ContactForm()
        return render(request, 'acbApp/contact.html', context = {'msg': msg, 'form':form })
    return redirect('/')

cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def login(request):
    return render(request, 'acbApp/login.html')


cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def viewMessage(request):
    data = FeedbackModel.objects.all()
    return render(request, 'acbApp/viewmessage.html', context={'data':data})

def aboutus(request):
    return render(request, 'acbApp/aboutus.html')

def comPro(request):
    return render(request, 'acbApp/comPro.html')

def onGoingPro(request):
    return render(request, 'acbApp/ongoingpro.html')

def delete(request,id):
    queryset = FeedbackModel.objects.get(id=id)
    queryset.delete()
    return redirect('/viewmessage/')