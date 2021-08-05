from store.models import Category


# this will be available in every single page
def categories(request):
  return {'categories': Category.objects.all()}
