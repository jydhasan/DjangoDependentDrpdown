# Generated by Django 3.2.9 on 2021-11-12 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ajax', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ajax.category')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ajax.subcategory')),
            ],
        ),
    ]
