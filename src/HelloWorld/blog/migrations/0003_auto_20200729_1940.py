# Generated by Django 2.1.5 on 2020-07-29 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200729_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='index',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='Untitled', max_length=120),
        ),
    ]