from django.conf import settings
from django.core.mail import send_mail   
from django.shortcuts import render
from .forms import ContactForm,SignUpForm

# Create your views here.
def home(request):
	tittle='welcome'
	form=SignUpForm(request.POST or None)
	context={
		"tittle":tittle,
		"form":form
	}
	if form.is_valid():
		instance=form.save(commit=False)
		full_name=form.cleaned_data.get("full_name")
		if not full_name:
			full_name="new full name"
		instance.full_name=full_name
		instance.save()
		context={
			"tittle":"thank you"
		}
	
	
	return render(request,"example_fluid.html",context)
def home1(request):
	return render(request,"home1.html",{})
def contact(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():
		#for key,value in form.cleaned_data.iteritems():
		#	print key,value
		form_email=form.cleaned_data.get("email")
		form_message=form.cleaned_data.get("message")
		form_full_name=form.cleaned_data.get("full_name")
		#print email,message,full_name
		subject='site contact form'
		from_email=settings.EMAIL_HOST_USER
		to_email=[from_email,'youotheremail@gmail.com']
		contact_message="%s:%s via %s"%(
					form_full_name, 
					form_message,
					form_email)
		#some_html_message="""
		#<h1>hello</h1>
		#"""
		send_mail(subject,
			contact_message,	
			from_email,
			to_email,
			#html_message=some_html_message,
			fail_silently=True)
	context={
		"form":form,
	}
	return render(request,"form.html",context)

		
