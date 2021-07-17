# Generated by Django 3.2.2 on 2021-05-27 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impactfee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('usetypename', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterModelTable(
            name='servicearea',
            table='impactfee_servicearea',
        ),
    ]