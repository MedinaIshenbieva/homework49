# Generated by Django 4.0.1 on 2022-01-13 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuetracker',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='statuses', to='webapp.status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='issuetracker',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='types', to='webapp.type', verbose_name='Тип'),
        ),
    ]
