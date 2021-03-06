# Generated by Django 3.2.3 on 2021-05-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='fb_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='ig_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='tw_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='yt_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='img',
            field=models.ImageField(null=True, upload_to='org_img'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='mail',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='phone',
            field=models.IntegerField(unique=True),
        ),
    ]
