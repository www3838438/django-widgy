# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-15 16:23
from __future__ import unicode_literals

from django.db import migrations, models, connection


def convert_to_uuid(apps, schema_editor):
    if connection.vendor != 'postgresql':
        return

    with connection.cursor() as cursor:
        cursor.execute(
            """
            ALTER TABLE "form_builder_emailuserhandler" ALTER COLUMN "to_ident" TYPE uuid USING to_ident::uuid;
            ALTER TABLE "form_builder_formsubmission" ALTER COLUMN "form_ident" TYPE uuid USING form_ident::uuid;
            ALTER TABLE "form_builder_formvalue" ALTER COLUMN "field_ident" TYPE uuid USING field_ident::uuid;
            ALTER TABLE "form_builder_fieldmappingvalue" ALTER COLUMN "field_ident" TYPE uuid USING field_ident::uuid;
            """
        )


class Migration(migrations.Migration):

    dependencies = [
        ('form_builder', '0004_auto_20171115_1556'),
    ]

    operations = [
        migrations.RunPython(convert_to_uuid, lambda apps, schema_editor: None),
        migrations.AlterField(
            model_name='emailuserhandler',
            name='to_ident',
            field=models.UUIDField(null=True, verbose_name='to'),
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='form_ident',
            field=models.UUIDField(),
        ),
        migrations.AlterField(
            model_name='formvalue',
            name='field_ident',
            field=models.UUIDField(),
        ),
        migrations.AlterField(
            model_name='fieldmappingvalue',
            name='field_ident',
            field=models.UUIDField(null=True),
        ),
    ]
