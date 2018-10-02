from random import randint

import barcode
from PIL import Image
from barcode.writer import ImageWriter
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .barcode import create_composite_barcode_image
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
            try:
                guest_instance = Guest.objects.get(pk=badge_number)
            except ObjectDoesNotExist:
                status = "Not a registered guest"
                messages.error(request, status)
                return HttpResponseRedirect(request.path)

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


def bartest(request, num_selection=5):

    badge_numbers = [e.badge_number for e in Guest.objects.all()]

    for i in range(num_selection):
        selection = badge_numbers[randint(0, len(badge_numbers) - 1)]

        code128 = barcode.get_barcode_class('code128')
        code = code128(selection, writer=ImageWriter())

        barcode_image = code.save('checkin/static/checkin/tmp/ean8_barcode' + str(i))

    create_composite_barcode_image()

    response = HttpResponse(content_type="image/png")

    image = Image.open('checkin/static/checkin/tmp/master.png')
    image.save(response, 'PNG')

    return response
