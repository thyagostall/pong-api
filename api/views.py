from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, Http404

from api.models import Score


def convert(score):
    return {
        'player': score.player,
        'computer': score.computer,
        'name': score.name,
        'timestamp': score.timestamp,
    }

def get_high_scores():
    scores = Score.objects.extra(
        select={'difference': 'player - computer'}
    ).order_by('-difference', '-timestamp')[:10]

    result = {i: convert(score) for i, score in enumerate(scores)}
    return JsonResponse({'high_score': result})

def post_score(parameters):
    player = parameters['player']
    computer = parameters['computer']
    name = parameters['name']

    score = Score(player=player, computer=computer, name=name)
    score.save()

    result = {'result': 'success'}
    return JsonResponse(result)

@csrf_exempt
def score(request):
    if request.method == 'GET':
        return get_high_scores()
    elif request.method == 'POST':
        return post_score(request.POST)
    else:
        raise Http404('Invalid method.')
