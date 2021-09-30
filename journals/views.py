from django.http import HttpResponse, FileResponse
from django.views.generic import ListView
from django.shortcuts import render
from django.core.exceptions import MultipleObjectsReturned

from journals.models import Publication
from accounts.models import Publisher


class PublicationsView(ListView):
    model = Publication
    template_name = 'publications_list.html'
    
    def get_queryset(self, publisher): # new
        query = self.request.GET.get('q')
        query = query if query else ''
        object_list = Publication.objects.filter(publisher__title=publisher, title__icontains=query)
        return object_list

    def get(self, request, publisher):
        page_link = request.get_full_path().split('?')[0]
        object_list = self.get_queryset(publisher)
        publisher_object = Publisher.objects.get(title=publisher)
        return render(
            request,
            'publications_list.html',
            {'link_to_this_page': page_link, 'publisher': publisher_object, 'object_list': object_list}
        )


class SearchResultsView(ListView):
    model = Publication
    template_name = 'search_results.html'
    paginate_by = 10

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Publisher.objects.filter(title__icontains=query)
        return object_list


class PublishersView(ListView):
    model = Publisher
    template_name = 'publishers_list.html'
    paginate_by = 10


def publication_serve_view(request, publisher, publication):
    try:
        publication = Publication.objects.get(title=publication, publisher__title=publisher)
        return FileResponse(publication.pdf)
    except MultipleObjectsReturned:
        return render(request, 'message.html', {'message': 'خطایی در یافتن نشریه‌ی مورد نظر به وجود آمده‌است.'})
