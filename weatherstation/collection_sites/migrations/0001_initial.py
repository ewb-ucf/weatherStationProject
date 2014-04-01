# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sensor'
        db.create_table(u'collection_sites_sensor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dataType', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('modelnumber', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('input_pin', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('data_rate', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('collection_freq', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('read_time', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('write_file', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('last_collection_time', self.gf('django.db.models.fields.CharField')(default='0', max_length=200)),
        ))
        db.send_create_signal(u'collection_sites', ['Sensor'])

        # Adding model 'WeatherData'
        db.create_table(u'collection_sites_weatherdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sitename', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('dataType', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collection_sites.Sensor'], null=True)),
        ))
        db.send_create_signal(u'collection_sites', ['WeatherData'])

        # Adding model 'WeatherCollectionSystem'
        db.create_table(u'collection_sites_weathercollectionsystem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('sitename', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('data', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collection_sites.WeatherData'], null=True)),
            ('about', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'collection_sites', ['WeatherCollectionSystem'])


    def backwards(self, orm):
        # Deleting model 'Sensor'
        db.delete_table(u'collection_sites_sensor')

        # Deleting model 'WeatherData'
        db.delete_table(u'collection_sites_weatherdata')

        # Deleting model 'WeatherCollectionSystem'
        db.delete_table(u'collection_sites_weathercollectionsystem')


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
            'about': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
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