from django.shortcuts import render
from .models import Part
from .forms import AddPartForm


def part_add_view(request):
    form = AddPartForm()
    context = {
        'form': form,
    }
    print(dir(request.GET))
    if request.method == 'POST':
        form = AddPartForm(request.POST)
        if form.is_valid():
            part_object = form.save()
            # nazwa = from.cleaned_data.get('nazwa')
            # opis = from.cleaned_data.get('opis')
            # ilość = from.cleaned_data.get('ilość')
            # kupione_od = from.cleaned_data.get('kupione_od')
            # dodane = from.cleaned_data.get('dodane')
    return render(request, 'parts/add.html', context=context)

def part_edit_view(request, id=None):
    part_obj = None
    if id is not None:
        part_obj = Part.objects.get(id=id)
    context = {
        'object': part_obj,
    }
    # print(part_obj.nazwa)

    if request.method == 'POST':        
        part_obj.nazwa= request.POST.get("nazwa"),
        if request.POST.get("nazwa") != '':
            part_obj.nazwa= request.POST.get("nazwa")
         
        if request.POST.get("ilość")!= '':
            part_obj.ilość = request.POST.get("ilość")
        if request.POST.get("opis")!= '':
            part_obj.opis = request.POST.get("opis")
        if request.POST.get("kupione_od") != '':
            part_obj.kupione_od = request.POST.get("kupione_od")
        part_obj.save()

 
    return render(request, 'parts/edit.html', context= context)


# Create your views here.
