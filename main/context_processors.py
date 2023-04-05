import json

from .models import MainCategory
from .models import SubCategory


def add_variable_to_context(request):
    category = []
    main_category = MainCategory.objects.all()
    sub_category = SubCategory.objects.all()

    for cat in main_category:
        dict_cat = dict()
        dict_cat['id'] = cat.id
        dict_cat['name'] = cat.name
        sub = sub_category.filter(category_id=cat.id)
        dict_all_sub = []
        for each in sub:
            dict_sub = dict()
            dict_sub['id'] = each.id
            dict_sub['name'] = each.name
            dict_all_sub.append(dict_sub)

        dict_cat['sub'] = dict_all_sub
        category.append(dict_cat)


    return {
        'category': category,
    }
