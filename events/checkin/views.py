from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import CheckInForm

from .models import Guest


def index(request):
    return render(request, 'checkin/index.html',)


def overview(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def checkin(request):
    if request.method == 'POST':
        form = CheckInForm(request.POST)

        check_in_form = CheckInForm(request.POST)
        if check_in_form.is_valid():
            badge_number = check_in_form.cleaned_data['badge_number']
            guest_instance = get_object_or_404(Guest, pk=badge_number)
            # make just show an error message

            if not guest_instance.is_checked_in:
                guest = Guest.objects.get(pk=badge_number)
                guest.is_checked_in = True
                guest.save()

                status = guest.name + " is successfully checked in"
                messages.success(request, status)

            else:
                status = guest_instance.name + " is already checked in!"
                messages.error(request, status)

            return HttpResponseRedirect(request.path)

    else:
        check_in_form = CheckInForm()

    context = {
        'form': check_in_form
    }

    return render(request, 'checkin/index.html', context)
