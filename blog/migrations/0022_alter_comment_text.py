# Generated by Django 4.1.7 on 2023-03-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(),
        ),
    ]
