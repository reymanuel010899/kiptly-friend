# Generated by Django 4.2 on 2023-04-15 03:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solisitudmodel',
            name='solisitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_solicitud_reverse', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solisitudmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitud_reverse', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_user_reverse', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notificacionesmodels',
            name='amigo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='notificacion_amigo_reverse', to='home.amigomodels'),
        ),
        migrations.AddField(
            model_name='notificacionesmodels',
            name='comentarios',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Comentariosreverse', to='home.comentarmodels'),
        ),
        migrations.AddField(
            model_name='notificacionesmodels',
            name='like',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_noti', to='home.likemodels'),
        ),
        migrations.AddField(
            model_name='notificacionesmodels',
            name='solicitud',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitud_notificaciones_reverce', to='home.solisitudmodel'),
        ),
        migrations.AddField(
            model_name='notificacionesmodels',
            name='solicitud_enviada',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitud_enviada', to='home.amigomodels'),
        ),
        migrations.AddField(
            model_name='notificacionesmodels',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_reverce', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notificacionesmodels',
            name='usuarios',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios_reverce', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='likemodels',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_post_reverse', to='home.postmodel'),
        ),
        migrations.AddField(
            model_name='likemodels',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_user_reverse', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conpartirmodels',
            name='amigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conpartir_amigos_reverce', to='home.amigomodels'),
        ),
        migrations.AddField(
            model_name='conpartirmodels',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concartir_post_riverse', to='home.postmodel'),
        ),
        migrations.AddField(
            model_name='conpartirmodels',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conpatir_user_reverse', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentarmodels',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario_post_reverse', to='home.postmodel'),
        ),
        migrations.AddField(
            model_name='comentarmodels',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario_user_reverse', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentariolike',
            name='comentario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario_like_model', to='home.comentarmodels'),
        ),
        migrations.AddField(
            model_name='comentariolike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario_user_like_reverse', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chatvistomodels',
            name='amigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Amigochatview', to='home.amigomodels'),
        ),
        migrations.AddField(
            model_name='chatvistomodels',
            name='mensaje',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='chatvistamodel', to='home.chatmodels'),
        ),
        migrations.AddField(
            model_name='chatmodels',
            name='amigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amigo_chats_reverse', to='home.amigomodels'),
        ),
        migrations.AddField(
            model_name='chatmodels',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_chats_reverse', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='amigomodels',
            name='añadidos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='añadidos_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='amigomodels',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_añadidos', to=settings.AUTH_USER_MODEL),
        ),
    ]
