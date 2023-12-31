# Generated by Django 4.2.5 on 2023-09-15 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='band',
            options={'verbose_name': 'Band', 'verbose_name_plural': 'Bands'},
        ),
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band')),
            ],
        ),
    ]
