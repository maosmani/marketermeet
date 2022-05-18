# Generated by Django 3.2.6 on 2021-08-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0003_studentmeetings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetings',
            name='field',
        ),
        migrations.AddField(
            model_name='meetings',
            name='area',
            field=models.CharField(choices=[('Applications and Real-Time Area', 'Applications and Real-Time Area'), ('General Area', 'General Area'), ('Internet Area', 'Internet Area'), ('Operations and Management Area  ', 'Operations and Management Area '), ('Routing Area ', 'Routing Area '), ('Security Area', 'Security Area'), ('Transport Area', 'Transport Area')], default='choose your field', max_length=100),
        ),
    ]
