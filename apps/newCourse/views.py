from django.shortcuts import render, redirect
from .models import Course
# Create your views here.

def index(request):
	context = {
		'courseNames': Course.objects.all(),
	}
	return render(request, 'newCourse/index.html', context)

def addCourse(request):
	if request.method == 'POST':
		name = Course.objects.create(name=request.POST['name'], description=request.POST['description'])
		id = name.id
		print id
	context = {
		"id": id,
	}
	return redirect('/', context)

def remove(request, id):
	print "remove"
	if request.session == "GET":
		messages.error(request, "NOPE")
		return redirect('/')
	context = {
		'courseNames':Course.objects.get(id=id)
	}
	return render(request, 'newCourse/remove.html', context)

def delete(request):
	Course.objects.get(id=request.POST['id']).delete()
	return redirect('/')