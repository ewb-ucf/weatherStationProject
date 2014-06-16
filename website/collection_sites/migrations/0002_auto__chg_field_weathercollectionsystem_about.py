# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'WeatherCollectionSystem.about'
        db.alter_column(u'collection_sites_weathercollectionsystem', 'about', self.gf('django.db.models.fields.CharField')(max_length=500))

    def backwards(self, orm):

        # Changing field 'WeatherCollectionSystem.about'
        db.alter_column(u'collection_sites_weathercollectionsystem', 'about', self.gf('django.db.models.fields.CharField')(max_length=1000))

    models = {
        u'collection_sites.sensor': {
            'Meta': {'object_name': 'Sensor'},
            'collection_freq': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'dataType': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'data_rate': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'input_pin': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'last_collection_time': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '200'}),
            'modelnumber': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'read_time': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'write_file': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
        },
        u'collection_sites.weathercollectionsystem': {
            'Meta': {'object_name': 'WeatherCollectionSystem'},
            'about': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'data': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['collection_sites.WeatherData']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'sitename': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'collection_sites.weatherdata': {
            'Meta': {'object_name': 'WeatherData'},
            'dataType': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['collection_sites.Sensor']", 'null': 'True'}),
            'sitename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'value': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['collection_sites']