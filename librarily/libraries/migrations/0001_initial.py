# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import livefield.fields
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('uuid', django_extensions.db.fields.PostgreSQLUUIDField(editable=False, primary_key=True, serialize=False, db_column='id', blank=True)),
                ('live', livefield.fields.LiveField(default=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthorBook',
            fields=[
                ('uuid', django_extensions.db.fields.PostgreSQLUUIDField(editable=False, primary_key=True, serialize=False, db_column='id', blank=True)),
                ('live', livefield.fields.LiveField(default=True)),
                ('author', models.ForeignKey(to='libraries.Author')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('uuid', django_extensions.db.fields.PostgreSQLUUIDField(editable=False, primary_key=True, serialize=False, db_column='id', blank=True)),
                ('live', livefield.fields.LiveField(default=True)),
                ('title', models.CharField(max_length=128)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('authors', models.ManyToManyField(to='libraries.Author', through='libraries.AuthorBook')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('uuid', django_extensions.db.fields.PostgreSQLUUIDField(editable=False, primary_key=True, serialize=False, db_column='id', blank=True)),
                ('live', livefield.fields.LiveField(default=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('uuid', django_extensions.db.fields.PostgreSQLUUIDField(editable=False, primary_key=True, serialize=False, db_column='id', blank=True)),
                ('live', livefield.fields.LiveField(default=True)),
                ('address', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='place',
            unique_together=set([('address', 'city', 'state', 'live')]),
        ),
        migrations.AddField(
            model_name='library',
            name='place',
            field=models.ForeignKey(to='libraries.Place'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='library',
            unique_together=set([('place', 'live')]),
        ),
        migrations.AddField(
            model_name='book',
            name='library',
            field=models.ForeignKey(to='libraries.Library'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='authorbook',
            name='book',
            field=models.ForeignKey(to='libraries.Book'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='libraries.Book', through='libraries.AuthorBook'),
            preserve_default=True,
        ),
    ]
