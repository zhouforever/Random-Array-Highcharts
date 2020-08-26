import json
import random

from django.http import JsonResponse

from app01 import models


def db_handler(array, No=[6, ]):
    keys = ['val%s' % i for i in range(1, 1+No[0])]
    return dict(zip(keys, array))


def dynamic_data(request, number=6):
    data_array = []
    for i in range(1, 1+number):
        data_array.append(random.randint(0, 100))
    models.TableOne.objects.create(**db_handler(data_array, [number, ]))
    print(data_array)
    return JsonResponse(data_array,  safe=False)


def serialize_o(data, many=False):
    def serialize_data(obj):
        return [obj.val1, obj.val2, obj.val3, obj.val4, obj.val5, obj.val6]
    if many:
        data_list = []
        for obj in data:
            data_list.append(serialize_data(obj))
        return data_list
    return serialize_data(data)


def reverse_backup_data():
    return models.TableTwo.objects.all().order_by('-id')


def backup_data(request):
    def my_data():
        data = json.loads(request.body.decode('utf-8'))
        return data['array']

    def de_duplication():
        last_obj = reverse_backup_data().first()
        last_data = serialize_o(last_obj)
        return last_data == my_data()

    if request.method == 'POST':
        msg = 'Data saved successfully!'
        vals = my_data()
        if not de_duplication():
            models.TableTwo.objects.create(**db_handler(vals))
        else:
            msg = 'Data has been captured. Skip '
        return JsonResponse(msg, safe=False)


def backup_show(request, limits=100):
    data_list = reverse_backup_data()
    print("data >>> ", len(data_list), data_list)

    demand_data = data_list
    if data_list.count() > limits:
        demand_data = data_list[0:limits]

    return JsonResponse(serialize_o(demand_data, many=True), safe=False)



