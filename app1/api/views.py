from django.shortcuts import render
from django.http import HttpResponse
import string
import random

# Create your views here.
def generate_password(r):
    l=8
    ch=string.ascii_letters + string.digits
    p=''.join(random.choice(ch) for i in range(l))
    return HttpResponse(p)
