# Generated by Django 4.0.7 on 2022-08-24 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noticia', '0006_remove_noticia_titulo_cartel_noticia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='categoria',
            field=models.IntegerField(choices=[('Cursos', 'Cursos'), ('Informacion', 'Informacion'), ('Ingresos', 'Ingresos'), ('Ambiental', 'Ambiental'), ('Deportes', 'Deportes')], default=1),
        ),
    ]
