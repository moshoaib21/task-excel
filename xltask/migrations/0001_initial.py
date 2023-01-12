# Generated by Django 4.1.5 on 2023-01-12 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_num', models.IntegerField()),
                ('dep_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=70)),
                ('lastname', models.CharField(max_length=70)),
                ('gender', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=200)),
                ('salary', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xltask.department')),
            ],
        ),
    ]
