from django.views.generic import ListView
from django.shortcuts import render

from journals.models import Publication
from accounts.models import Publisher


class PublicationsView(ListView):
    model = Publication
    template_name = 'publications_list.html'
    
    def get(self, request, publisher):
        object_list = Publication.objects.filter(publisher__title__icontains=publisher)
        return render(
            request,
            'publications_list.html',
            {'publisher': publisher, 'object_list': object_list}
        )


class PublishersView(ListView):
    model = Publisher
    template_name = 'publishers_list.html'
