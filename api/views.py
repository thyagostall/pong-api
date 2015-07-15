from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, Http404


@csrf_exempt
def score(request):
    if request.method == 'GET':
        return JsonResponse({'high_score': 1000})
    elif request.method == 'POST':
        return JsonResponse({'high_score': 5000})
    else:
        raise Http404('Invalid method.')
