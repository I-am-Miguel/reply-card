# Generated by Django 2.0 on 2018-06-13 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turma', '0002_auto_20180612_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='alunos',
            field=models.ManyToManyField(blank=True, null=True, to='aluno.Aluno'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='sessoes',
            field=models.ManyToManyField(blank=True, null=True, to='turma.Sessao'),
        ),
    ]
