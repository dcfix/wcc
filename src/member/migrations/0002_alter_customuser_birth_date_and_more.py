# Generated by Django 4.2.7 on 2023-11-26 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(blank=True, help_text='We only track birthday month and year, so day will be set to the 2st. ', null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_active_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='member_since',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='quick_checkin',
            field=models.CharField(blank=True, help_text='A shortcut code for checking in', max_length=10, null=True),
        ),
    ]
