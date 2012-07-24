# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AssignmentTemplate'
        db.create_table('assignment_assignmenttemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('objectives', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('prompt', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('rubric', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('assignment', ['AssignmentTemplate'])

        # Adding model 'Assignment'
        db.create_table('assignment_assignment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['course.Course'])),
            ('created_from', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['assignment.AssignmentTemplate'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('objectives', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('prompt', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('rubric', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('assignment', ['Assignment'])

        # Adding model 'SyllabusTemplate'
        db.create_table('assignment_syllabustemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('assignment', ['SyllabusTemplate'])

        # Adding model 'Syllabus'
        db.create_table('assignment_syllabus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['course.Course'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('assignment', ['Syllabus'])


    def backwards(self, orm):
        # Deleting model 'AssignmentTemplate'
        db.delete_table('assignment_assignmenttemplate')

        # Deleting model 'Assignment'
        db.delete_table('assignment_assignment')

        # Deleting model 'SyllabusTemplate'
        db.delete_table('assignment_syllabustemplate')

        # Deleting model 'Syllabus'
        db.delete_table('assignment_syllabus')


    models = {
        'assignment.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.Course']"}),
            'created_from': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assignment.AssignmentTemplate']"}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'objectives': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'prompt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rubric': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'assignment.assignmenttemplate': {
            'Meta': {'object_name': 'AssignmentTemplate'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'objectives': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'prompt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rubric': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'assignment.syllabus': {
            'Meta': {'object_name': 'Syllabus'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'course_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.Course']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'assignment.syllabustemplate': {
            'Meta': {'object_name': 'SyllabusTemplate'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'course.course': {
            'Meta': {'object_name': 'Course'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dept': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'room_no': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['assignment']