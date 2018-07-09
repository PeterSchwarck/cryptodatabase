# Generated by Django 2.0.7 on 2018-07-07 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocurrency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noftification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_delta', models.FloatField()),
                ('price_delta', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=20)),
                ('phone', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.FloatField()),
                ('price', models.FloatField()),
                ('market_cap', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='coin',
            name='current_coin_value',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='delta',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='email',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='market_cap',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='price',
        ),
        migrations.RemoveField(
            model_name='coin',
            name='volume',
        ),
        migrations.AddField(
            model_name='ticker',
            name='coin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cryptocurrency.Coin'),
        ),
        migrations.AddField(
            model_name='noftification',
            name='coin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cryptocurrency.Coin'),
        ),
        migrations.AddField(
            model_name='noftification',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cryptocurrency.Session'),
        ),
    ]
