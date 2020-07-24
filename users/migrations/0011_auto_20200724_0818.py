# Generated by Django 2.2.5 on 2020-07-24 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pants', '0001_initial'),
        ('tops', '0001_initial'),
        ('shoes', '0001_initial'),
        ('users', '0010_auto_20200724_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pants',
            field=models.ManyToManyField(related_name='pants', to='pants.Pants'),
        ),
        migrations.AddField(
            model_name='user',
            name='shoes',
            field=models.ManyToManyField(related_name='shoes', to='shoes.Shoes'),
        ),
        migrations.AddField(
            model_name='user',
            name='tops',
            field=models.ManyToManyField(related_name='tops', to='tops.Tops'),
        ),
    ]
