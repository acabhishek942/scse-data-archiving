# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'OtherStaff.image'
        db.add_column(u'store_details_otherstaff', 'image',
                      self.gf('stdimage.models.StdImageField')(max_length=100, null=True, variations={}),
                      keep_default=False)

        # Adding field 'Student.image'
        db.add_column(u'store_details_student', 'image',
                      self.gf('stdimage.models.StdImageField')(max_length=100, null=True, variations={}),
                      keep_default=False)

        # Adding field 'Faculty.image'
        db.add_column(u'store_details_faculty', 'image',
                      self.gf('stdimage.models.StdImageField')(max_length=100, null=True, variations={}),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'OtherStaff.image'
        db.delete_column(u'store_details_otherstaff', 'image')

        # Deleting field 'Student.image'
        db.delete_column(u'store_details_student', 'image')

        # Deleting field 'Faculty.image'
        db.delete_column(u'store_details_faculty', 'image')


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
            'image': ('stdimage.models.StdImageField', [], {'max_length': '100', 'null': 'True', u'variations': '{}'}),
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
            'image': ('stdimage.models.StdImageField', [], {'max_length': '100', 'null': 'True', u'variations': '{}'}),
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
            'image': ('stdimage.models.StdImageField', [], {'max_length': '100', 'null': 'True', u'variations': '{}'}),
            'joining_year': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'land_line': ('django.db.models.fields.IntegerField', [], {}),
            'mobile_number': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'projects': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['store_details']