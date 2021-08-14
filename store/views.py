from django.shortcuts import get_object_or_404, render

# Create your views here.
from store.models import Category, Product


def product_list(request):
  products = Product.objects.prefetch_related("product_image").filter(
      is_active=True)
  return render(request, 'store/index.html', {'products': products})


def product_detail(request, slug):
  product = get_object_or_404(Product, slug=slug, is_active=True)
  return render(request, 'store/single.html', {'product': product})


def category_list(request, category_slug=None):
  category = get_object_or_404(Category, slug=category_slug)

  try:
    slugs = [
        c['slug']
        for c in category.get_descendants(include_self=True).values('slug')
    ]
    products = Product.objects.filter(category__slug__in=slugs)
  except Exception:
    products = Product.objects.filter(category__slug=category_slug)

  return render(request, 'store/category.html', {
      'category': category,
      'products': products
  })
