# Generated by Django 4.0.4 on 2022-05-02 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=500, unique=True, verbose_name='이메일'),
        ),
    ]