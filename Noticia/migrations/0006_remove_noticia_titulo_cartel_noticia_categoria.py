# Generated by Django 4.0.7 on 2022-08-21 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noticia', '0005_alter_comment_noticia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='titulo_cartel',
        ),
        migrations.AddField(
            model_name='noticia',
            name='categoria',
            field=models.IntegerField(choices=[(1, 'Cursos'), (2, 'Informacion'), (3, 'Ingresos')], default=1),
        ),
    ]