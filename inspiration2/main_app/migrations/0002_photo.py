# Generated by Django 4.1.1 on 2022-09-21 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=400)),
                ('inspiration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.inspiration')),
            ],
        ),
    ]
