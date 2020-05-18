# Generated by Django 3.0.6 on 2020-05-18 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20200516_1405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bug',
            options={'ordering': ('-open_date',)},
        ),
        migrations.AlterModelOptions(
            name='worknote',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterField(
            model_name='bug',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='worknote',
            name='description',
            field=models.TextField(),
        ),
    ]