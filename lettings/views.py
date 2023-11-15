from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Display an index with a list of :model:`lettings.letting`.

    **Context**

    ``lettings_list``
        A list of instances of :model:`lettings.letting`.

    **Template:**

    :template:`lettings/index.html`

    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Display an individual letting of :model:`lettings.letting`.

    **Context**

    ``letting``
        An instance of :model:`lettings.letting` containing a title and
        an address.

    **Template:**

    :template:`letting.html`

    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
