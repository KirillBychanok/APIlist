# Generated by Django 4.0.5 on 2022-07-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterField(
            model_name='tickets',
            name='is_active',
            field=models.CharField(choices=[('a', 'Активно'), ('о', 'Отложено'), ('з', 'Закрыто')], default='a', max_length=1),
        ),
    ]
