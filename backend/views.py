from backend.forms import ImageForm, ImageForm2
from backend.predict import predict, predict_com
from django.contrib.auth import authenticate, login, logout
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
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
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
        form2 = ImageForm2(request.POST, request.FILES)
        if form.is_valid():
            if form2.is_valid():
                image_obj = form.save()
                image_url = image_obj.image.url
                image_obj2 = form2.save()
                image2_url = image_obj2.image2.url
                output = predict_com(("." + image_url), ("." + image2_url))
                compare_flag = "Yes"
            else:
                image_obj = form.save()
                image_url = image_obj.image.url
                output = predict("." + image_url)
                compare_flag = "No"

            est_water = output['est_water']
            est_land = output['est_land']
            bin_water = output['bin_water']
            bin_land = output['bin_land']
            est_image = output['est']
            bin_image = output['bin']
            height = output['height']
            width = output['width']

            if compare_flag == "No":
                return render(request, "backend/admin.html",
                              {'form': form, 'form2': form2, 'imageURL': image_url, 'bin_water': bin_water,
                               'bin_land': bin_land,
                               'est_water': est_water, 'est_land': est_land, 'est_image': est_image,
                               'bin_image': bin_image,
                               'height': height, 'width': width, 'post': "Yes", 'compare_flag': compare_flag})
            else:
                est_water_com = output['est_water_com']
                est_land_com = output['est_land_com']
                bin_water_com = output['bin_water_com']
                bin_land_com = output['bin_land_com']
                est_image_com = output['est_com']
                bin_image_com = output['bin_com']
                bin_water_diff = output['bin_water_diff']
                est_water_diff = output['est_water_diff']
                return render(request, "backend/admin.html",
                              {'form': form, 'form2': form2, 'imageURL': image_url, 'bin_water': bin_water,
                               'bin_land': bin_land, 'est_water': est_water, 'est_land': est_land,
                               'est_image': est_image, 'bin_image': bin_image,
                               'height': height, 'width': width, 'image2URL': image2_url,
                               'bin_water_com': bin_water_com, 'bin_land_com': bin_land_com,
                               'est_water_com': est_water_com, 'est_land_com': est_land_com,
                               'est_image_com': est_image_com, 'bin_image_com': bin_image_com,
                               'bin_water_diff': bin_water_diff, 'est_water_diff': est_water_diff,
                               'post': "Yes", 'compare_flag': compare_flag})

        else:
            print("Form is invalid.")
        return render(request, "backend/admin.html", {'form': form, 'form2': form2, 'post': "No"})
    form = ImageForm
    form2 = ImageForm2
    return render(request, "backend/admin.html", {'form': form, 'form2': form2, 'post': "No"})


def logoutUser(request):
    logout(request)
    return redirect('home')
