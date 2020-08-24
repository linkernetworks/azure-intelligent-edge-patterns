# Generated by Django 3.0.8 on 2020-08-24 08:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('voe_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('download_uri', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('training_counter', models.IntegerField(default=0)),
                ('setting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voe_settings.Setting', to_field='uuid')),
            ],
        ),
    ]
