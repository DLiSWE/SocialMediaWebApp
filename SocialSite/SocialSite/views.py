from django.views.generic import TemplateView, ListView
from Posts.models import Post

class TestPage(TemplateView):
    template_name = "test.html"

class ThanksPage(TemplateView):
    template_name = "thanks.html"

class HomePage(TemplateView):
    template_name = 'index.html'

class SearchPage(ListView):
    template_name = 'search_for.html'
    model = Post

    def get_queryset(self):
        result = super(SearchPage, self).get_queryset()
        query = self.request.GET.get('search')
        field = query
        if query:
            postresult = Post.objects.filter(message__icontains=query)
            result = postresult
        else:
            result = None
        return result

    