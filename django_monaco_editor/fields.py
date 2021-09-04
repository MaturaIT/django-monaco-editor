from django import forms
#
from .widgets import MonacoEditorWidget


class MonacoEditorField(forms.CharField):
    def __init__(self, language="markdown", *args, **kwargs):
        super(MonacoEditorField, self).__init__(*args, **kwargs)
        if not issubclass(self.widget.__class__, MonacoEditorWidget):
            self.widget = MonacoEditorWidget(language=language)


class MonacoEditorJsonField(forms.JSONField):
    def __init__(self, language="json", *args, **kwargs):
        super(MonacoEditorJsonField, self).__init__(*args, **kwargs)
        if not issubclass(self.widget.__class__, MonacoEditorWidget):
            self.widget = MonacoEditorWidget(language=language)
