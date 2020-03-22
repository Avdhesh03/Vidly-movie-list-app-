# Generated by Django 3.0.4 on 2020-03-22 07:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('release_year', models.IntegerField()),
                ('number_in_stock', models.IntegerField()),
                ('rating', models.FloatField()),
                ('daily_rate', models.FloatField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Genre')),
            ],
        ),
    ]
