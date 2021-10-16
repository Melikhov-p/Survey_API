# Generated by Django 3.2.8 on 2021-10-16 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='main.choice', verbose_name='выбор'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='choice_text',
            field=models.CharField(max_length=200, null=True, verbose_name='текст выбора'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='main.question', verbose_name='вопрос'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey', to='main.survey', verbose_name='опрос'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=150, verbose_name='текст выбора'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='main.question', verbose_name='вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=150, verbose_name='текст вопроса'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(max_length=1, verbose_name='тип вопроса'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='end_date',
            field=models.DateTimeField(verbose_name='дата окончания'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата начала'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='survey_description',
            field=models.CharField(max_length=150, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='survey_name',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
    ]
