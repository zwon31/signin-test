# Generated by Django 4.1.5 on 2023-01-23 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="bookPost",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                ("publisher", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("content", models.TextField()),
                ("hits", models.PositiveIntegerField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="bookComment",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("comment", models.TextField()),
                (
                    "book_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.bookpost"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="account.user"
                    ),
                ),
            ],
        ),
    ]
