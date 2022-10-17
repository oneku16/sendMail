from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.contrib import messages
from django.template.loader import render_to_string
from django.conf import settings


def hello(request):
	return HttpResponse("<h1>hello<h1>")


def summ(request):
	return HttpResponse("<h1>5+1<h1>")


def mail(request):
	html_temp = render_to_string('d1.html', {'name': 'eku'})
	email = EmailMessage(
		"qwe",
		html_temp,
		settings.EMAIL_HOST_USER,
		[
		'eku.ulanov@yandex.com',
		'elnazar.ulanbekuulu_2025@ucentralasia.org',
		'ilkhomzhon.sidikov_2025@ucentralasia.org',
		'eku.ulanov@gmail.com',
		]
		)
	email.fail_silently = False
	email.send()
	return render(request, 'd1.html', {'name': 'elnazar'})