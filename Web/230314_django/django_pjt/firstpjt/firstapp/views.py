from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(
        """
        <h1> 첫 Django PJT </h1>
        <p>My name is Ethan</p>
        <p>My phone number is 010-xxxx-xxxx</p>
        <p>Seoul Ssafy</p>
        <p>My name is Aiden</p>

        
        """
        )

