# Generated by Django 2.2.7 on 2019-11-26 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=20, null=True)),
                ('student_email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FaceImagesVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagesvideo_data', models.FileField(null=True, upload_to='media/video')),
                ('imagesvideo_name', models.CharField(default='Noname', max_length=20, null=True)),
                ('datevideo_upload', models.DateTimeField(auto_now_add=True, null=True)),
                ('student_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student_info.Student')),
            ],
        ),
    ]
