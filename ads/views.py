from django.http import JsonResponse
import json

from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ads, Categories
from func import json_data_cat


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads_ = Ads.objects.all()
        search_text = request.GET.get("text", None)
        if search_text:
            ads_ = ads_.filter(text=search_text)

        response = []
        for ad_ in ads_:
            response.append({
                "id": ad_.id,
                "name": ad_.name,
                "author": ad_.author,
                "price": ad_.price,
                "description": ad_.description,
                "address": ad_.address,
                "is_published": ad_.is_published,
            })
        return JsonResponse(response, safe=False)  # json_dumps_params={"ensure_ascii" : False}

    def post(self, request):
        ad_data = json.loads(request.body)

        ad_ = Ads()
        ad_.name = ad_data["name"]
        ad_.author = ad_data["author"]
        ad_.price = ad_data["price"]
        ad_.description = ad_data["description"]
        ad_.address = ad_data["address"]
        ad_.is_published = ad_data["is_published"]

        ad_.save()

        return JsonResponse({
            "id": ad_.id,
            "name": ad_.name,
            "author": ad_.author,
            "price": ad_.price,
            "description": ad_.description,
            "address": ad_.address,
            "is_published": ad_.is_published,
        })
@method_decorator(csrf_exempt, name='dispatch')
class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        try:
            ad_ = self.get_object()

        except :
            return JsonResponse({"Ошибка": "Запись не найдена"}, status=404)

        return JsonResponse({
            "id": ad_.id,
            "name": ad_.name,
            "author": ad_.author,
            "price": ad_.price,
            "description": ad_.description,
            "address": ad_.address,
            "is_published": ad_.is_published,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()
        search_text = request.GET.get("text", None)
        if search_text:
            categories = categories.filter(text=search_text)

        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name
            })
        return JsonResponse(response, safe=False)  # json_dumps_params={"ensure_ascii" : False}

    def post(self, request):
        category_data = json.loads(request.body)

        category = Categories()
        category.name = category_data["name"]

        category.save()

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })


    def datas_cat(self, request):
        category_data = json.loads(json_data_cat)

        for cat in category_data:
            category = Categories()
            category.id = cat["id"]
            category.name = cat["name"]

            category.save()

            return JsonResponse({
                    "id": category.id,
                    "name": category.name
                })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Categories.DoesNotExist:
            return JsonResponse({"Ошибка": "Запись не найдена"}, status=404)

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


