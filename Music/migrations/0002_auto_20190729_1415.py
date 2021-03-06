# Generated by Django 2.1.7 on 2019-07-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='description',
            field=models.TextField(default='Listen and get me the feedback'),
        ),
        migrations.AlterField(
            model_name='music',
            name='cover_image',
            field=models.ImageField(upload_to='media/songCoverFolder'),
        ),
    ]
