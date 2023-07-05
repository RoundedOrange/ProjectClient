from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'main.html')
def personal_info(request):
    return render(request,'personal_info.html')