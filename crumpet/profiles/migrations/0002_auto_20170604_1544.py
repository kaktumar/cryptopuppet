# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 15:44
from __future__ import unicode_literals

import crumpet.profiles.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('available', crumpet.profiles.fields.AmountField(decimal_places=8, default=0, max_digits=30)),
                ('on_orders', crumpet.profiles.fields.AmountField(decimal_places=8, default=0, max_digits=30)),
                ('btc_value', crumpet.profiles.fields.AmountField(decimal_places=8, default=0, max_digits=30)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balances', to='profiles.UserAccount')),
            ],
            options={
                'db_table': 'poloniex_balance',
                'ordering': ['-created'],
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('ticker', models.CharField(max_length=30, verbose_name='Ticker Symbol')),
                ('status', models.CharField(choices=[('open', 'open'), ('cancelled', 'cancelled'), ('processed', 'processed')], db_index=True, default=None, max_length=255)),
                ('order_number', models.CharField(max_length=50, verbose_name='Order Number')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='profiles.UserAccount')),
            ],
            options={
                'db_table': 'poloniex_order',
                'ordering': ['-created'],
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_id', models.CharField(max_length=20)),
                ('last', crumpet.profiles.fields.AmountField(decimal_places=8, default=0, max_digits=30)),
                ('lowest_ask', crumpet.profiles.fields.AmountField(decimal_places=8, default=0, max_digits=30)),
                ('highest_bid', crumpet.profiles.fields.AmountField(decimal_places=8, default=0, max_digits=30)),
                ('percent_change', crumpet.profiles.fields.PercentField(decimal_places=3, max_digits=8)),
                ('base_volume', crumpet.profiles.fields.AmountField(decimal_places=8, default=0, max_digits=30)),
                ('quote_volume', crumpet.profiles.fields.AmountField(decimal_places=8, default=0, max_digits=30)),
                ('is_frozen', models.BooleanField()),
                ('high_24_hour', crumpet.profiles.fields.AmountField(decimal_places=8, default=0, max_digits=30)),
                ('low_24_hour', crumpet.profiles.fields.AmountField(decimal_places=8, default=0, max_digits=30)),
            ],
            options={
                'db_table': 'poloniex_ticker',
                'ordering': ['-percent_change'],
                'get_latest_by': 'percent_change',
            },
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', crumpet.profiles.fields.AmountField(decimal_places=8, default=0, max_digits=30)),
                ('rate', crumpet.profiles.fields.AmountField(decimal_places=8, default=0, max_digits=30)),
                ('price', crumpet.profiles.fields.PriceField(decimal_places=2, default=0, max_digits=30)),
                ('amount', crumpet.profiles.fields.AmountField(decimal_places=8, default=0, max_digits=30)),
                ('type', models.IntegerField(choices=[(0, 'buy'), (1, 'sell')], db_index=True, max_length=255)),
                ('date', models.DateTimeField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trades', to='profiles.Order')),
            ],
        ),
        migrations.CreateModel(
            name='TradingStrategyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FixedStrategyProfile',
            fields=[
                ('tradingstrategyprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.TradingStrategyProfile')),
                ('buy', crumpet.profiles.fields.PriceField(decimal_places=2, default=0, max_digits=30)),
                ('sell', crumpet.profiles.fields.PriceField(decimal_places=2, default=0, max_digits=30)),
            ],
            options={
                'db_table': 'strategy_profile_fixed',
            },
            bases=('profiles.tradingstrategyprofile',),
        ),
        migrations.CreateModel(
            name='RelativeStrategyProfile',
            fields=[
                ('tradingstrategyprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.TradingStrategyProfile')),
                ('buy', crumpet.profiles.fields.PercentField(decimal_places=3, max_digits=8)),
                ('sell', crumpet.profiles.fields.PercentField(decimal_places=3, max_digits=8)),
            ],
            options={
                'db_table': 'strategy_profile_relative',
            },
            bases=('profiles.tradingstrategyprofile',),
        ),
        migrations.AddField(
            model_name='tradingstrategyprofile',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserAccount'),
        ),
    ]
