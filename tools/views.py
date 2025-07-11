from django.shortcuts import render

def tools_index(request):
    return render(request, 'tools/tools_index.html')
