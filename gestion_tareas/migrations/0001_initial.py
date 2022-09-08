# Generated by Django 4.1 on 2022-09-08 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="usuario",
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
                ("nombre", models.CharField(default="", max_length=128)),
                ("apellido", models.CharField(default="", max_length=128)),
                ("codigo_usuario", models.CharField(default="", max_length=128)),
                ("contraseña", models.CharField(default="", max_length=128)),
            ],
        ),
    ]