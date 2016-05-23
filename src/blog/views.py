from django.shortcuts import render, HttpResponse
from .forms import AccountForm
from .models import Account
from datetime import datetime

html = """<html>
		<body>
			<h1>Hello %s</h1>
			<p>%s</p>
		</body>
		</html>"""

def Home(request):
	if request.method == "POST":
		login = AccountForm(request.POST or None)
		if login.is_valid():
			"""Account.objects.create(
				username=login.cleaned_data["username"],
				password=login.cleaned_data["password"],
				email=login.cleaned_data["email"]
				)"""
			p = Account(
				username=login.cleaned_data["username"],
				password=login.cleaned_data["password"],
				email=login.cleaned_data["email"])
			p.username += "000001"
			p.save()
			timenow = datetime.now()
			return HttpResponse(html %(login.cleaned_data["username"],timenow))
			#return HttpResponse("Welcome %s" %login.cleaned_data["username"])
	login = AccountForm()
	return render(request,'home.html',{"login":login})

def Page(request,offset):
	number = int(offset)
	next_number = number+1
	array = []
	for i in range(0,number):
		array.append(i)
	return render(request,'page.html',{"number":number,"next_number":next_number,"array":array})

