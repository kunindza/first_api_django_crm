# Generated by Django 3.2.8 on 2021-11-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'Contact'), ('2', 'Potential'), ('3', 'Paying'), ('4', 'Lost')], default='1', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='e_mail',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='mobile_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
