# Generated by Django 4.2.16 on 2024-11-22 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0004_financialproductlike'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cur_unit', models.TextField()),
                ('cur_nm', models.TextField()),
                ('ttb', models.TextField(blank=True, null=True)),
                ('tts', models.TextField(blank=True, null=True)),
                ('deal_bas_r', models.TextField(blank=True, null=True)),
                ('bkpr', models.TextField(blank=True, null=True)),
                ('yy_efee_r', models.TextField(blank=True, null=True)),
                ('ten_dd_efee_r', models.TextField(blank=True, null=True)),
                ('kftc_bkpr', models.TextField(blank=True, null=True)),
                ('kftc_deal_bas_r', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
