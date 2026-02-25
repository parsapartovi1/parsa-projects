from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Input
# Create your views here.



class InputBox(View):
    def get(self, request):
        return render(request, "main_page.html")

    def post(self, request):
        text = request.POST.get("user_input")

        input_instance = Input()
        result = input_instance.maker(text)

        context = {
            "original_text": text,
            "converted_text": result,
        }

        return render(request, "main_page.html" , context)