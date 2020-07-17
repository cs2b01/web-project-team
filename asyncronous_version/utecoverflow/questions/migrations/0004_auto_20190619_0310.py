# Generated by Django 2.2.2 on 2019-06-19 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20190614_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='content',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions.Question'),
        ),
    ]