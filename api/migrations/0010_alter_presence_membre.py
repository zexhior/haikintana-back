# Generated by Django 3.2 on 2021-06-17 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210617_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presence',
            name='membre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presencemembre', to='api.membre'),
        ),
    ]
