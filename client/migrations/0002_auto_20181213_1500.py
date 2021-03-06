# Generated by Django 2.1.1 on 2018-12-13 15:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookissue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ACCNO', models.CharField(max_length=16)),
                ('UID', models.CharField(max_length=120, null=True)),
                ('ED', models.DateTimeField(default=datetime.datetime(2018, 12, 20, 15, 0, 20, 508926))),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='AC',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='Count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='FA',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookissue',
            name='Book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Book'),
        ),
    ]
