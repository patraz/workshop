# Generated by Django 3.2.8 on 2021-10-19 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('opis', models.CharField(max_length=150)),
                ('ilość', models.IntegerField(default=0)),
                ('kupione_od', models.TextField()),
                ('dodane', models.DateField()),
            ],
        ),
    ]