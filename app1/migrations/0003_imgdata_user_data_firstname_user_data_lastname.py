# Generated by Django 4.1.4 on 2023-01-05 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_usernam_user_data_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='imgdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_data', models.FileField(upload_to='')),
                ('desc', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='user_data',
            name='firstname',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='user_data',
            name='lastname',
            field=models.CharField(default=0, max_length=50),
        ),
    ]