from django.db import models
import uuid
import random
class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class meta:
        abstract = True
class Types(BaseModel):
    gfg_name = models.CharField(max_length=100)
    def __str__(self)-> str:
        return self.gfg_name
class Question(BaseModel):
    gfg = models.ForeignKey(Types,related_name='gfg', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)
    def __str__(self)-> str:
        return self.question
    def get_answers(self):
        answer_objs= list(Answer.objects.filter(question=self))
        data = []
        random.shuffle(answer_objs)
        for answer in answer_objs:
            data.append({
                'answer' :answer_obj.answer, 
                'is_correct' : answer_obj.is_correct
            })
        return data
class Answer(BaseModel):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    def __str__(self)-> str:
        return self.answer