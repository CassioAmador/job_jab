# Generated by Django 4.1 on 2022-09-05 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0002_alter_job_doc_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='job',
            name='doc_id',
            field=models.CharField(max_length=255),
        ),
    ]