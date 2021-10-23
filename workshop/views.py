# Rendering html web pages
#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.shortcuts import render, redirect

from parts.models import Part



def home_view(request, *args, **kwargs,):
    """
    Take in a request(Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    if request.user.is_authenticated:
        # from the database??
        part_obj = Part.objects.get(id=1)
        parts_q = Part.objects.all()
        # print(request, args, kwargs)
        # print(request.GET)
        query_dict = request.GET
        query = query_dict.get('query')
        if query is not None:
            print(query)
            parts_q = Part.objects.filter(opis__icontains=query)
            print(parts_q)
        context = {
            "parts_q" : parts_q,
            "title" : part_obj.nazwa,
            'quantity': part_obj.ilość,
            "content" : part_obj.opis,
            "id" : part_obj.id,
            'supplier': part_obj.kupione_od
            }
        return render(request, 'home-view.html', context=context)
    return redirect('/login')