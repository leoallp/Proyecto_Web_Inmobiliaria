# Generated by Django 5.0.6 on 2024-07-07 21:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comuna",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="TipoInmueble",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="TipoUsuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Direccion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=255)),
                (
                    "comuna",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="arriendo_app.comuna",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="arriendo_app.region",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="comuna",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="arriendo_app.region"
            ),
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "rut",
                    models.CharField(max_length=9, primary_key=True, serialize=False),
                ),
                ("direccion", models.CharField(max_length=255)),
                ("telefono", models.CharField(max_length=50)),
                (
                    "tipo_usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="arriendo_app.tipousuario",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Inmueble",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("disponibilidad", models.BooleanField(default=False)),
                ("nombre", models.CharField(max_length=50)),
                ("descripcion", models.TextField()),
                ("m2_construidos", models.FloatField()),
                ("m2_totales_o_del_terreno", models.FloatField()),
                ("numero_de_estacionamientos", models.IntegerField(default=0)),
                ("numero_de_habitaciones", models.IntegerField(default=0)),
                ("numero_de_banios", models.IntegerField(default=0)),
                ("precio_mensual", models.FloatField()),
                (
                    "comuna",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="arriendo_app.comuna",
                    ),
                ),
                (
                    "direccion",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="arriendo_app.direccion",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="arriendo_app.region",
                    ),
                ),
                (
                    "tipo_inmueble",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="arriendo_app.tipoinmueble",
                    ),
                ),
                (
                    "usuarios",
                    models.ManyToManyField(
                        related_name="inmuebles", to="arriendo_app.usuario"
                    ),
                ),
            ],
        ),
    ]
