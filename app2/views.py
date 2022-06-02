from django.shortcuts import render

# Create your views here.
def teacher_signup(request):
    return render(request,'app2/signup.html')