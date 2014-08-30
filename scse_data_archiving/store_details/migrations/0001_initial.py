# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Faculty'
        db.create_table(u'store_details_faculty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('faculty_code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('current_subjects', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('research_interest', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('joining_year', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('projects', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('e_mail', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('mobile_number', self.gf('django.db.models.fields.IntegerField')()),
            ('land_line', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'store_details', ['Faculty'])

        # Adding model 'Student'
        db.create_table(u'store_details_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('entry_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('current_semester', self.gf('django.db.models.fields.IntegerField')()),
            ('joining_year', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('projects', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('e_mail', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('mobile_number', self.gf('django.db.models.fields.IntegerField')()),
            ('land_line', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'store_details', ['Student'])

        # Adding model 'OtherStaff'
        db.create_table(u'store_details_otherstaff', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('joining_year', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('e_mail', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('mobile_number', self.gf('django.db.models.fields.IntegerField')()),
            ('land_line', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'store_details', ['OtherStaff'])


    def backwards(self, orm):
        # Deleting model 'Faculty'
        db.delete_table(u'store_details_faculty')

        # Deleting model 'Student'
        db.delete_table(u'store_details_student')

        # Deleting model 'OtherStaff'
        db.delete_table(u'store_details_otherstaff')


    models = {
        u'store_details.faculty': {
            'Meta': {'object_name': 'Faculty'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'current_subjects': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'e_mail': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'faculty_code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joining_year': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'land_line': ('django.db.models.fields.IntegerField', [], {}),
            'mobile_number': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'projects': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'research_interest': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'store_details.otherstaff': {
            'Meta': {'object_name': 'OtherStaff'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'e_mail': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joining_year': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'land_line': ('django.db.models.fields.IntegerField', [], {}),
            'mobile_number': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'store_details.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'current_semester': ('django.db.models.fields.IntegerField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'e_mail': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'entry_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joining_year': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'land_line': ('django.db.models.fields.IntegerField', [], {}),
            'mobile_number': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'projects': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['store_details']