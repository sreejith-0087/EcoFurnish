from .models import Categories


def EcoFurnish_Category(request):
    cat = Categories.objects.all()
    return dict(cat=cat)

