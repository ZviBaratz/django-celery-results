# -*- coding: utf-8 -*-
# Generated by Django 2.2.4 on 2019-08-21 19:53

# this file is auto-generated so don't do flake8 on it
# flake8: noqa

from __future__ import absolute_import, unicode_literals

from django.db import migrations, models
import django.utils.timezone


def copy_date_done_to_date_created(apps, schema_editor):
    TaskResult = apps.get_model('django_celery_results', 'taskresult')
    db_alias = schema_editor.connection.alias
    TaskResult.objects.using(db_alias).all().update(
        date_created=models.F('date_done')
    )


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_results', '0005_taskresult_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskresult',
            name='date_created',
            field=models.DateTimeField(
                auto_now_add=True,
                db_index=True,
                default=django.utils.timezone.now,
                help_text='Datetime field when the task result was created in UTC',
                verbose_name='Created DateTime'
            ),
            preserve_default=False,
        ),
        migrations.RunPython(copy_date_done_to_date_created),
    ]