# Generated by Django 2.2 on 2020-07-14 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0002_auto_20200714_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('weekly_stipend', models.DecimalField(decimal_places=2, max_digits=7)),
                ('category', models.CharField(max_length=20)),
                ('agma', models.BooleanField()),
                ('housing', models.BooleanField()),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('logo', models.TextField(blank=True, null=True)),
                ('minimum_age', models.IntegerField(blank=True, null=True)),
                ('maximum_age', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_reviews', to='vocalist_app.Company')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_reviewed', to='user_app.User')),
            ],
        ),
    ]
