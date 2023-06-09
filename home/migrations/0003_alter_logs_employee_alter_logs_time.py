# Generated by Django 4.1.7 on 2023-04-16 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('home', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.employees', verbose_name='员工编号'),
        ),
        migrations.AlterField(
            model_name='logs',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='修改时间'),
        ),
    ]
