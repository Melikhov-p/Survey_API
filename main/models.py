from django.db import models

class Survey(models.Model):
    survey_name = models.CharField(max_length=150, verbose_name='Название')
    pub_date = models.DateTimeField(verbose_name='дата начала', auto_now_add=True)
    end_date = models.DateTimeField(verbose_name='дата окончания')
    survey_description = models.CharField(max_length=150, verbose_name='описание')

    def __str__(self):
        return self.survey_name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ['-id']


class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=150, verbose_name='текст вопроса')
    question_type = models.CharField(max_length=1, verbose_name='тип вопроса')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-id']

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE, verbose_name='вопрос')
    choice_text = models.CharField(max_length=150, verbose_name='текст выбора')

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Выбор'
        verbose_name_plural = 'Выборы'
        ordering = ['-id']

class Answer(models.Model):
    user_id = models.IntegerField()
    survey = models.ForeignKey(Survey, related_name='survey', on_delete=models.CASCADE, verbose_name='опрос')
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE, verbose_name='вопрос')
    choice = models.ManyToManyField(Choice, related_name='choice', verbose_name='выбор(-ы)')
    choice_text = models.CharField(max_length=200, null=True, verbose_name='текст выбора')

    def __str__(self):
        return self.question.question_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['-id']