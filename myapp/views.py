from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from bookstore import settings
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes 
from django.utils.encoding import force_str
from . tokens import generate_token


# Create your views here.

def home(request):
	return render(request, 'myapp/index.html')

def signup(request):

	if request.method == "POST":
		username = request.POST.get('username')
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']

		if User.objects.filter(username=username).exists():
			messages.error(request, "Username already exists.")
			return redirect('home')

		if User.objects.filter(email=email).exists():
			messages.error(request, "Email already exists.")
			return redirect('home')

		if len(username) > 20:
			messages.error(request, "Username must be under 10 characters.")

		if pass1 != pass2:
			messages.error(request, "Passwords do not match!")

		if not username.isalnum():
			messages.error(request, "Username must be alphanumeric.")
			return redirect('home')

		myuser = User.objects.create_user(username, email, pass1)
		myuser.first_name = fname
		myuser.last_name = lname
		myuser.is_active = False

		myuser.save()

		messages.success(request, "Accouct Created Successfully.")

		#Welcome Email
		subject = "Welcome to quizzy"
		message = "Hello "+ myuser.first_name + "!! \nThank you for visiting our website.\nSent you a confirmation email. Please confirm"
		from_email = settings.EMAIL_HOST_USER
		recipient_list = [email] 

		send_mail(subject, message, from_email, recipient_list, fail_silently=True)

		current_site = get_current_site(request)
		subject2 = "Confirm your identity"
		message2 = render_to_string('email_confirmation.html', {
			'name': myuser.first_name,
			'domain': current_site.domain,
			'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
			'token': generate_token.make_token(myuser)
		})
		email = EmailMessage(
				subject2,
				message2,
				settings.EMAIL_HOST_USER,
				[myuser.email],
			)
		email.fail_silently = True
		email.send()

		return redirect("signin")
	return render(request, 'myapp/signup.html')

def signin(request):

	if request.method == "POST":
		username = request.POST['username']
		pass1 = request.POST['pass1']

		user = authenticate(username=username, password=pass1)

		if user is not None:
			login(request, user)
			fname = user.first_name
			return render(request, 'myapp/dashboard.html', {'fname':fname})
		else:
			messages.error(request, "Bad Credentials.")
			return redirect('home')

	return render(request, 'myapp/signin.html')

def signout(request):
	if not request.user.is_authenticated:
		messages.success(request, "Already Logged Out")	
	else:
		logout(request)
		messages.success(request, "Logged Out")
	return redirect('home')

def activate(request, uidb64, token):
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		myuser = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		myuser = None

	if myuser is not None and generate_token.check_token(myuser, token):
		myuser.is_active = True
		myuser.save()
		login(request, myuser)
		return redirect('home')

	else:
		return render(request, 'authentication_failed.html')

#@login_required
def dashboard(request):
	#return render(request, 'myapp/dashboard.html')
	if not request.user.is_authenticated:
		messages.success(request, 'Please sign in')
		return redirect('signin')

	return render(request, 'myapp/dashboard.html')
	#current_user = request.user
	#user = User.objects.get(username = current_user)

	#return redirect('home')
    

    #product = Product.objects.all()#.order_by('-age')
    #part_name_filter = Product.objects.values_list('part_name', flat=True).distinct()
    #context = {'product': product, 'part_name_filter':part_name_filter}
    #return render(request, 'myapp/dashboard.html')#, context)
