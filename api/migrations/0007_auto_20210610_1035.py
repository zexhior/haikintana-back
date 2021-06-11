# Generated by Django 3.2 on 2021-06-10 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_membre_cotisation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactOrganisation',
        ),
        migrations.RemoveField(
            model_name='regle',
            name='activite',
        ),
        migrations.AlterField(
            model_name='presence',
            name='activite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activites', to='api.activite'),
        ),
        migrations.AlterField(
            model_name='presence',
            name='membre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membres', to='api.membre'),
        ),
        migrations.DeleteModel(
            name='Cotisation',
        ),
        migrations.DeleteModel(
            name='Regle',
        ),
    ]
