from django.shortcuts import render
from django.http import JsonResponse
from models import *
import random

def home(request):
    context = {'categories': Types.objects.all()}
    if request.Get.get('gfg'):
        return redirect(f"/quiz/?gfg={request.Get.get('gfg')}")
    return render(request, 'home.html', context)
def quiz(request):
    context = {'gfg':request.Get.get('gfg')}
    return render(request, 'quiz.html', context)

def get_quiz(request):
    try:
        question_objs= Question.objects.all()
        if request.Get.get('gfg'):
            question_objs = question_objs.filter(gfg__gfg_name__icontains=request.Get.get('gfg'))
            question_objs=list(question_objs)
            data = []
            random.shuffle(question_objs)

            for question_obj in question_objs:
                data.append({
                    "uid":question_obj.uid,
                    "gfg":question_obj.gfg.gfg_name,
                    "question":question_obj.question,
                    "marks": question_obj.marks,
                    "answer": question_obj.answer(),
                })
            payload = {'status':True,'data':data}
            return JsonResponse(payload)
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")
