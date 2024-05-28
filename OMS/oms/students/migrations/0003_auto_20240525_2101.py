# Generated by Django 3.2.25 on 2024-05-25 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0002_auto_20240525_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Course', models.CharField(max_length=100)),
                ('Year', models.IntegerField()),
                ('Username', models.CharField(max_length=100, unique=True)),
                ('Password', models.CharField(max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
                ('user', models.OneToOneField(max_length=10, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='StudentTable',
        ),
    ]