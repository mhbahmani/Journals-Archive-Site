from django.http import HttpResponse, FileResponse
from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Model

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


def publication_serve_view(request, publisher, publication):
    try:
        publication = Publication.objects.get(title=publication, publisher__title=publisher)
        return FileResponse(publication.pdf)
    except Model.MultipleObjectsReturned:
        return render(request, 'message.html', {'message': 'خطایی در یافتن نشریه‌ی مورد نظر به وجود آمده‌است.'})