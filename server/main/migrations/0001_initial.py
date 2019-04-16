# Generated by Django 2.1.7 on 2019-04-02 10:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=32)),
                ('atd_checked', models.IntegerField(default=1)),
                ('last_checked', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]