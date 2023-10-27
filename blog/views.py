import feedparser
import json
import re
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import User, Reply
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    request.session['previous_url'] = request.path
    return render(request, 'blog/index.html')

def signup(request):
    return render(request, 'blog/signup.html')

def blog_view(request):
    request.session['previous_url'] = request.path
    return render(request, 'blog/blog_view.html')

def submit_registration(request):
    
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('user_pw')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists() | User.objects.filter(email=email).exists():
            return JsonResponse({'status': 'error', 'error_detail': 'Username or email duplication error'})

        if len(password) < 8 or not re.search(r'[a-zA-Z]', password):
            return JsonResponse({'status': 'error', 'error_detail': 'Password policy error'})

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        message = 'Sign up Successful !'
        previous_url = request.session.get('previous_url', '/')

        return JsonResponse({'message': message, 'status': 'success', 'previous_url': previous_url})

def submit_signin(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
           
            username = data.get('user_name')
            password = data.get('user_pw')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                response_data = {'message': 'Login successful !', 'user_name': username}
                return JsonResponse(response_data)
            else:
                response_data = {'message': 'User not found'}
                return JsonResponse(response_data, status=401)

        except json.JSONDecodeError:
            response_data = {'message': 'Invalid JSON format'}
            return JsonResponse(response_data, status=400)

    return JsonResponse({'message': 'Invalid request method'}, status=405)

def signout(request):
    logout(request)
    return redirect('index')

def post_reply(request):
    if request.method == 'POST':
        reply = Reply(reply=request.POST.get('message'))
        reply.save()
        return render(request, 'blog/reply.html')    
    return render(request, 'blog/reply.html')

