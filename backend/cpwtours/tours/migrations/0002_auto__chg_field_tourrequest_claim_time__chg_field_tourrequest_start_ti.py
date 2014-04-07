# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'TourRequest.claim_time'
        db.alter_column(u'tours_tourrequest', 'claim_time', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'TourRequest.start_time'
        db.alter_column(u'tours_tourrequest', 'start_time', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'TourRequest.claim_time'
        db.alter_column(u'tours_tourrequest', 'claim_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(1, 1, 1, 0, 0)))

        # Changing field 'TourRequest.start_time'
        db.alter_column(u'tours_tourrequest', 'start_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(1, 1, 1, 0, 0)))

    models = {
        u'tours.tourrequest': {
            'Meta': {'object_name': 'TourRequest'},
            'claim_time': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'R'", 'max_length': '1'})
        }
    }

    complete_apps = ['tours']