# Generated by Django 4.2.16 on 2024-11-19 00:07

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
            name='FinancialProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('etc_note', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('join_way', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('product_type', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('rsrv_type_nm', models.TextField(blank=True, null=True)),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField()),
                ('save_trm', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option', to='financials.financialproducts')),
            ],
        ),
        migrations.CreateModel(
            name='FinancialComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('financial_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='financial_product_comments', to='financials.financialproducts')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='financial_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
