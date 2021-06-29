# Generated by Django 3.2 on 2021-06-28 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_photoprofil_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='url_image',
            field=models.CharField(default='', max_length=200),
        ),
    ]
