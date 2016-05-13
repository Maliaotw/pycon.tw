# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-03 13:42
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.text import slugify


def generate_slugs(apps, schema_editor):
    SponsoredEvent = apps.get_model('events', 'SponsoredEvent')
    db_alias = schema_editor.connection.alias
    slug_len = SponsoredEvent._meta.get_field('slug').max_length
    for e in SponsoredEvent.objects.using(db_alias).filter(slug=''):
        e.slug = slugify(e.title, allow_unicode=True)[:slug_len]
        e.save()


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsoredevent',
            name='slug',
            field=models.SlugField(
                allow_unicode=True, blank=True, verbose_name='slug',
            ),
        ),
        migrations.RunPython(
            code=generate_slugs,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name='sponsoredevent',
            name='slug',
            field=models.SlugField(allow_unicode=True, verbose_name='slug'),
        ),
    ]
