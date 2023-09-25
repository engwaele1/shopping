from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Member
from .form import MemberForm

# Create your views here.


# def members(request):
#     return HttpResponse("Hello world!")


# def members(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())


def members(request):
    mymembers = Member.objects.all().values()

    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MemberForm()

    template = loader.get_template('all_members.html')

    context = {
        'mymembers': mymembers, 'form': form
    }
    return HttpResponse(template.render(context, request))
    # context = {
    #     'mymembers': mymembers,
    # }
    # return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)

    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MemberForm()
    print('form wael')

    template = loader.get_template('details.html')
    context = {
        'mymember': mymember, 'form': form
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


# def testing(request):
#     mymembers = Member.objects.all().values()
#     template = loader.get_template('template.html')
#     context = {
#         'mymembers': mymembers,
#     }
#     return HttpResponse(template.render(context, request))


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['MY lovely kids', 'zeina', 'zahraa', 'Adam', 'Amir'],
    }
    return HttpResponse(template.render(context, request))


def template(request):

    template = loader.get_template('template.html')

    context = {
        'fruits': 'banaba',
    }
    return HttpResponse(template.render(context, request))
