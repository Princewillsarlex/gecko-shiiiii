# Generated by Django 2.2.7 on 2020-10-22 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Text')),
                ('done', models.BooleanField(default=False, verbose_name='Done')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todos',
                'ordering': ('-date_created',),
            },
        ),
    ]