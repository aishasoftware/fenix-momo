# Generated by Django 2.2.6 on 2019-10-24 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=50)),
                ('ramount', models.CharField(max_length=100)),
                ('rcurrency', models.CharField(max_length=50)),
                ('rexternalId', models.CharField(max_length=50)),
                ('rpartyIdType', models.CharField(max_length=50)),
                ('rpartyId', models.CharField(max_length=50)),
                ('rpayerMessage', models.CharField(max_length=50)),
                ('rpayeeNote', models.CharField(max_length=50)),
                ('rstatus', models.CharField(max_length=50)),
                ('rcreationTime', models.DateTimeField(blank=True, null=True)),
                ('rcompletionTime', models.DateTimeField(blank=True, null=True)),
                ('rresponseStatus', models.CharField(max_length=50)),
                ('rresponseMessage', models.CharField(max_length=50)),
                ('rresponseCode', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'MRequest',
            },
        ),
    ]