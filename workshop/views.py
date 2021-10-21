# Rendering html web pages
#

from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
import random

from parts.models import Part


def home_view(request, *args, **kwargs):
    """
    Take in a request(Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    # from the database??
    part_obj = Part.objects.get(id = 4)
    parts_q = Part.objects.all()
  

    context = {
        "parts_q" : parts_q,
        "title" : part_obj.nazwa,
        'quantity': part_obj.ilość,
        "content" : part_obj.opis,
        "id" : part_obj.id,
        'supplier': part_obj.kupione_od
        }

    HTML_STRING = render_to_string('home-view.html', context=context)

    return HttpResponse(HTML_STRING)