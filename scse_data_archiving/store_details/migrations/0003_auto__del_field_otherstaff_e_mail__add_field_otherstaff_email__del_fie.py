# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'OtherStaff.e_mail'
        db.delete_column(u'store_details_otherstaff', 'e_mail')

        # Adding field 'OtherStaff.email'
        db.add_column(u'store_details_otherstaff', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=254, unique=True, null=True),
                      keep_default=False)

        # Deleting field 'Student.e_mail'
        db.delete_column(u'store_details_student', 'e_mail')

        # Adding field 'Student.email'
        db.add_column(u'store_details_student', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=254, unique=True, null=True),
                      keep_default=False)

        # Deleting field 'Faculty.e_mail'
        db.delete_column(u'store_details_faculty', 'e_mail')

        # Adding field 'Faculty.email'
        db.add_column(u'store_details_faculty', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=254, unique=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'OtherStaff.e_mail'
        db.add_column(u'store_details_otherstaff', 'e_mail',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45, blank=True),
                      keep_default=False)

        # Deleting field 'OtherStaff.email'
        db.delete_column(u'store_details_otherstaff', 'email')

        # Adding field 'Student.e_mail'
        db.add_column(u'store_details_student', 'e_mail',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45, blank=True),
                      keep_default=False)

        # Deleting field 'Student.email'
        db.delete_column(u'store_details_student', 'email')

        # Adding field 'Faculty.e_mail'
        db.add_column(u'store_details_faculty', 'e_mail',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45, blank=True),
                      keep_default=False)

        # Deleting field 'Faculty.email'
        db.delete_column(u'store_details_faculty', 'email')


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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'unique': 'True', 'null': 'True'}),
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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'unique': 'True', 'null': 'True'}),
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