# Generated by Django 2.2 on 2020-07-21 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vocalist_app', '0007_correction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='correction',
            name='review',
        ),
        migrations.AddField(
            model_name='correction',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='has_corrections', to='vocalist_app.Company'),
        ),
    ]