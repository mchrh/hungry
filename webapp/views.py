from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import results

class HomePageView(TemplateView):
    template_name='index.html'

class SearchResultsView(ListView):
    model=results
    template_name='results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = results.objects.filter(
            Q(name__icontains=query) | Q(ING1__icontains=query)
        )
        return object_list

