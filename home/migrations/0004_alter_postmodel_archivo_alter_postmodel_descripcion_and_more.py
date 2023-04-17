# Generated by Django 4.2 on 2023-04-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_postmodel_archivo_alter_postmodel_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='archivo',
            field=models.FileField(upload_to='post/archivo'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='post/imagenes'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='post/videos'),
        ),
    ]