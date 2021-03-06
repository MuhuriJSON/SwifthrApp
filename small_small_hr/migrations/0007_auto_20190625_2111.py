# Generated by Django 2.1.7 on 2019-06-25 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("small_small_hr", "0006_auto_20181209_0108")]

    operations = [
        migrations.AlterField(
            model_name="annualleave",
            name="year",
            field=models.PositiveIntegerField(
                choices=[
                    (2017, 2017),
                    (2018, 2018),
                    (2019, 2019),
                    (2020, 2020),
                    (2021, 2021),
                    (2022, 2022),
                    (2023, 2023),
                    (2024, 2024),
                    (2025, 2025),
                    (2026, 2026),
                    (2027, 2027),
                    (2028, 2028),
                ],
                db_index=True,
                default=2017,
                verbose_name="Year",
            ),
        )
    ]
