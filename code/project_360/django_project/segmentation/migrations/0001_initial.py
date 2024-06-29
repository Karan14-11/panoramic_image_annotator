# Generated by Django 3.2.24 on 2024-04-17 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('label', '0001_initial'),
        ('api', '0008_saveddata_project_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='SegAnnotations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_no', models.SmallIntegerField()),
                ('coordinates', models.TextField()),
                ('image', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.saveddata')),
                ('label_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='label.label')),
            ],
        ),
    ]
