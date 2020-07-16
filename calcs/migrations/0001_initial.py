# Generated by Django 3.0.5 on 2020-05-20 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ohms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_needed', models.CharField(choices=[('voltage', 'Voltage'), ('current', 'Current'), ('resistance', 'Resistance')], default='voltage', max_length=20)),
                ('voltage', models.IntegerField()),
                ('current', models.IntegerField()),
                ('resistance', models.IntegerField()),
            ],
        ),
    ]