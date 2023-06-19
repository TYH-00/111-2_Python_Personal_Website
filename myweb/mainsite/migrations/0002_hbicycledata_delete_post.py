# Generated by Django 4.1.7 on 2023-05-25 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HBicycleData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sna', models.CharField(max_length=100)),
                ('sbi', models.IntegerField(default=0)),
                ('tot', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-sbi',),
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
