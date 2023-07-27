# Generated by Django 4.2.3 on 2023-07-27 07:26

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
            name='Gem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gem_name', models.CharField(max_length=30, verbose_name='Название камня')),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(verbose_name='Сумма')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deals.gem', verbose_name='Камень')),
            ],
        ),
    ]