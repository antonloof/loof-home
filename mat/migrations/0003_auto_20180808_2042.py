# Generated by Django 2.0.8 on 2018-08-08 18:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mat', '0002_auto_20180808_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_1_to_unit_2_factor', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversion', to='mat.Ingredient')),
                ('unit_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_1', to='mat.Unit')),
                ('unit_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_2', to='mat.Unit')),
            ],
        ),
        migrations.AlterField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(related_name='recipes', to='mat.Category'),
        ),
    ]