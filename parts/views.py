from django.shortcuts import render
from .models import Part

def part_edit_view(request, id=None):
    part_obj = None
    if id is not None:
        part_obj = Part.objects.get(id=id)
    context = {
        'object': part_obj,
    }
    return render(request, 'parts/edit.html', context= context)


# Create your views here.
