# Generated by Django 4.2 on 2023-05-03 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('number_of_working_hours', models.PositiveSmallIntegerField()),
                ('salary', models.PositiveIntegerField(default=0)),
                ('execution_status', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_job', to='users.customeruser')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status_order', models.BooleanField(default=True)),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='executor_employer', to='users.employeruser')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_job', to='job.job')),
            ],
        ),
    ]
