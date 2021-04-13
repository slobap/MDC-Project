# Generated by Django 3.2 on 2021-04-13 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='project',
            new_name='project_title',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='task',
        ),
        migrations.CreateModel(
            name='All',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tag')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.task')),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='tasks',
            field=models.ManyToManyField(through='myapp.All', to='myapp.Task'),
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(through='myapp.All', to='myapp.Tag'),
        ),
    ]