# Generated by Django 4.2.6 on 2023-10-12 18:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0003_alter_group_name_alter_teacher_subject"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("groups", models.ManyToManyField(to="school.group")),
            ],
        ),
    ]