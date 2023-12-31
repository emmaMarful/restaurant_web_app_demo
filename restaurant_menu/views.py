from django.shortcuts import render
from .models import Item, Meal_Category
from django.views import generic


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meal"] = Meal_Category
        return context


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"


def about(request):
    return render(request, "about.html")

