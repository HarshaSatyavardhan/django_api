# Generated by Django 3.2.7 on 2022-01-31 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='researchpapercontent',
        ),
        migrations.AddField(
            model_name='researchpaper',
            name='abstract',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='researchpaper',
            name='codes',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='researchpaper',
            name='discussion',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='researchpaper',
            name='methodology',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='researchpaper',
            name='result',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='researchpaper',
            name='system',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='researchpaper',
            name='link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
