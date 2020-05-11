# Generated by Django 3.0.5 on 2020-05-10 18:11

from django.db import migrations


def create_questions(apps, schema_editor):
    Question = apps.get_model("learning", "Question")
    Question.objects.create(question="miły", answer="nice")
    Question.objects.create(question="hojny", answer="generous")
    Question.objects.create(question="możliwe", answer="possible")
    Question.objects.create(question="niezależny", answer="independent")
    Question.objects.create(question="ciekawy", answer="curious")


class Migration(migrations.Migration):

    dependencies = [("learning", "0003_question_right_answer_id")]

    operations = [migrations.RunPython(create_questions)]
