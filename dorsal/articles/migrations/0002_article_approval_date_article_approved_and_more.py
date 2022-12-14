# Generated by Django 4.0.7 on 2022-08-22 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='approval_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='needs_approval',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='pretext',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='section',
            field=models.CharField(choices=[('UNA', 'unassigned'), ('SCT', 'at scitech'), ('PIT', 'in pittsburgh'), ('POL', 'politics'), ('TEC', 'technology'), ('SPT', 'sports'), ('BLG', 'blog')], default='UNA', max_length=3),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
