# Generated by Django 4.1.3 on 2022-11-29 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_transacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
