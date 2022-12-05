#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#fiche.py
import appModuleHandler
import controlTypes
import speech

class AppModule(appModuleHandler.AppModule):

    def event_valueChange(self, obj, nextHandler):
        if obj.role ==( controlTypes.ROLE_EDITABLETEXT if not hasattr(controlTypes, "Role") else controlTypes.Role.EDITABLETEXT)  and( controlTypes.STATE_READONLY if not hasattr(controlTypes, "State") else controlTypes.State.READONLY) in obj.states:
            speech.speakObject(obj, reason=controlTypes.REASON_CHANGE if hasattr(controlTypes, "REASON_CHANGE") else controlTypes.OutputReason.CHANGE)
        nextHandler



    def event_nameChange(self, obj, nextHandler):
        parent = obj.parent
        if parent.name == u'nom' or parent.name == u't\xe9l\xe9phone' or parent.name == u'fax' or parent.name == u'mail' or parent.name == u'adresse' or parent.name == u'note':
            speech.speakMessage(parent.name)
        nextHandler
