# Generated by Django 4.1.3 on 2022-11-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='cpf',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
