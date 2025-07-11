from django.shortcuts import render

def view_resume(request):
    return render(request, 'resume/view_resume.html')
