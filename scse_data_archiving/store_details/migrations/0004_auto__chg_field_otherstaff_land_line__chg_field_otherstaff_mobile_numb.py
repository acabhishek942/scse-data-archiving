# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'OtherStaff.land_line'
        db.alter_column(u'store_details_otherstaff', 'land_line', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'OtherStaff.mobile_number'
        db.alter_column(u'store_details_otherstaff', 'mobile_number', self.gf('django.db.models.fields.CharField')(max_length=13))

        # Changing field 'Student.land_line'
        db.alter_column(u'store_details_student', 'land_line', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Student.mobile_number'
        db.alter_column(u'store_details_student', 'mobile_number', self.gf('django.db.models.fields.CharField')(max_length=13))

        # Changing field 'Faculty.land_line'
        db.alter_column(u'store_details_faculty', 'land_line', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Faculty.mobile_number'
        db.alter_column(u'store_details_faculty', 'mobile_number', self.gf('django.db.models.fields.CharField')(max_length=13))

    def backwards(self, orm):

        # Changing field 'OtherStaff.land_line'
        db.alter_column(u'store_details_otherstaff', 'land_line', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'OtherStaff.mobile_number'
        db.alter_column(u'store_details_otherstaff', 'mobile_number', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Student.land_line'
        db.alter_column(u'store_details_student', 'land_line', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Student.mobile_number'
        db.alter_column(u'store_details_student', 'mobile_number', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Faculty.land_line'
        db.alter_column(u'store_details_faculty', 'land_line', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Faculty.mobile_number'
        db.alter_column(u'store_details_faculty', 'mobile_number', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'store_details.faculty': {
            'Meta': {'object_name': 'Faculty'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'current_subjects': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'unique': 'True', 'null': 'True'}),
            'faculty_code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('stdimage.models.StdImageField', [], {'max_length': '100', 'null': 'True', u'variations': '{}'}),
            'joining_year': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'land_line': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('stdimage.models.StdImageField', [], {'max_length': '100', 'null': 'True', u'variations': '{}'}),
            'joining_year': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'land_line': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'unique': 'True', 'null': 'True'}),
            'entry_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('stdimage.models.StdImageField', [], {'max_length': '100', 'null': 'True', u'variations': '{}'}),
            'joining_year': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'land_line': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'projects': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['store_details']