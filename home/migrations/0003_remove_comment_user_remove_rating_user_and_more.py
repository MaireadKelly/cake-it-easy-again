# Generated by Django 5.1.2 on 2024-10-22 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_comment_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='home.customer'),
        ),
        migrations.AddField(
            model_name='rating',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='home.customer'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='category',
            field=models.CharField(choices=[('wedding', 'Wedding'), ('birthday', 'Birthday'), ('anniversary', 'Anniversary'), ('baby_shower', 'Baby Shower'), ('Communion', 'Communion'), ('Confirmation', 'Confirmation'), ('other', 'Other')], default='other', max_length=50),
        ),
    ]
