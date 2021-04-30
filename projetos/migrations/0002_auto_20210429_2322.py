# Generated by Django 3.2 on 2021-04-29 23:22

from django.db import migrations

from projetos.models import TagChoices


def adicionar_tags(apps, schema_editor):
    Tag = apps.get_model('projetos', 'Tag')
    for id, _ in TagChoices.choices:
        Tag.objects.create(id=id)


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(adicionar_tags),
    ]
