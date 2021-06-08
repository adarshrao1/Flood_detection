from backend.forms import ImageForm
from backend.predict import predict
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render, redirect
from django.contrib import messages
from backend.forms import CreateUserForm
from django.contrib.auth.decorators import login_required


# Create your views here

def home(request):
    # render function takes argument - request
    # and return HTML as response
    return render(request, "backend/index.html")

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form }
        return render(request, 'backend/registration.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('admin')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('admin')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'backend/login.html', context)


@login_required(login_url='login')
def adminpage(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_obj = form.save()
            image_url = image_obj.image.url
            output = predict("."+image_url)

            est_water = output['est_water']
            est_land = output['est_land']
            bin_water = output['bin_water']
            bin_land = output['bin_land']
            est_image = output['est'][1:]
            bin_image = output['bin'][1:]
            height = output['height']
            width = output['width']

            return render(request, "backend/admin.html",
                          {'form': form, 'imageURL': image_url, 'bin_water': bin_water, 'bin_land': bin_land,
                           'est_water': est_water, 'est_land': est_land, 'est_image': est_image, 'bin_image': bin_image,
                           'height': height, 'width': width, 'post': "Yes"})
        else:
            print("problem!!!")
        return render(request, "backend/admin.html", {'form': form, 'post': "No"})
    form = ImageForm
    return render(request, "backend/admin.html", {'form': form, 'post': "No"})

def logoutUser(request):
    logout(request)
    return redirect('home')
