#from django.shortcuts import render, redirect
#from django.contrib.auth.models import User, auth
#from django.contrib import messages

#def home(request):

#    return render(request, 'home.html')
#def login(request):
 #   if request.method == 'POST':
  #      username = request.POST['username']
   #     password = request.POST['password']
    #    user = auth.authenticate(username=username, password=password)
     #   if user is not None:
      #      auth.login(request, user)
       #     return redirect('home')
        #else:
         #   messages.error(request, 'password not match')
          #  return redirect('register')
    #return render(request, 'login.html')


#def register(request):
 #   if request.method == 'POST':
  #      username = request.POST['username']
   #     email = request.POST['email']
    #    password = request.POST['password']
     #   password1 = request.POST['password1']
      #  if password == password1:
       #     if User.objects.filter(username=username).exists():
        #        messages.error(request, 'Username already exist')
         #   elif User.objects.filter(email = email).exists():
          #      messages.error(request, 'Email already exist')
           # else:
            #   user=User.objects.create_user(username=username, password=password, email=email)
             #  user.save();
              # return redirect('login')
        #else:
         #   messages.error(request,'password & password1 not matched')
    #return render(request, 'register.html')

#def logout(request):
 #   return redirect('login')