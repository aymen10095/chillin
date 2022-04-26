# Generated by Django 4.0.1 on 2022-04-09 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcd', '0002_activity_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='plan_activity',
            field=models.ManyToManyField(related_name='plan_activity', to='pcd.Activity'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('notification', models.TextField(max_length=500)),
                ('is_seen', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcd.user')),
            ],
        ),
    ]
