from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response

from contact.forms import ContactForm

def contact(request):
    # errors = []
    # if request.method == 'POST':
    #     if not request.POST.get('subject', ''):
    #         errors.append('Enter a subject')
    #     if not request.POST.get('message', ''):
    #         errors.append('Enter a message')
    #     if request.POST.get('email') and '@' not in request.POST['email']:
    #         errors.append('Enter a valid email address')
    #     if not errors:
    #         #send_mail(
    #         #        request.POST['subject'],
    #         #        request.POST['message'],
    #         #        request.POST.get('email', 'noreply@example.com'),
    #         #        ['jizhouli@126.com'],
    #         #        )
    #         return HttpResponseRedirect('/contact/thanks/')
    # return render_to_response('contact_form.html', {'errors': errors})

    form = ContactForm(
            initial = {'subject': 'default title'},
            )
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #send_mail(
            #        cd['subject'],
            #        cd['message'],
            #        cd.get('email', 'noreply@example.com'),
            #        ['jizhouli@126.com'],
            #        )
            return HttpResponseRedirect('/contact/thanks/')
        #else:
        #    form = ContactForm()
    return render_to_response('contact_form.html', {'form': form})

def contact_thanks(request):
    return HttpResponse("Thanks for contacting Justin!")

