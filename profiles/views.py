from django.shortcuts import render
from .models import Profile


def profiles_index(request):
    """
    Display an index with a list of :model:`profiles.profile`.

    **Context**

    ``profiles_list``
        A list of instances of :model:`profiles.profile`.

    **Template:**

    :template:`profiles_index.html`

    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Display an individual profile of :model:`profiles.profile`.

    **Context**

    ``profile``
        An instance of :model:`profiles.profile`.

    **Template:**

    :template:`letting.html`

    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
