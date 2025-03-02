from django.utils.html import format_html, mark_safe
from wagtail.admin.panels import Panel

class ReadOnlyPanel(Panel):
    def __init__(self, attr, style=None, add_hidden_input=False, *args, **kwargs):
        if not isinstance(attr, str):
            raise TypeError("attr must be a string")
        self.attr = attr
        self.style = style
        self.add_hidden_input = add_hidden_input
        super().__init__(*args, **kwargs)
        
    def clone(self):
        return self.__class__(
            attr=self.attr,
            heading=self.heading,
            classname=self.classname,
            help_text=self.help_text,
            style=self.style,
            add_hidden_input=self.add_hidden_input,
        )
    
    class BoundPanel(Panel.BoundPanel):
        def get_value(self):
            try:
                value = getattr(self.instance, self.panel.attr)
                if callable(value):
                    value = value()
                return value
            except AttributeError:
                return 'ERROR'

        def get_context_data(self, parent_context=None):
            context = super().get_context_data(parent_context)
            return {
                **context,
                'field_name': self.panel.attr,
                'heading': self.panel.heading or self.panel.attr.replace('_', ' ').title(),
                'value': self.get_value(),
                'help_text': self.panel.help_text,
                'style': mark_safe(f'style="{self.panel.style}"') if self.panel.style else '',
                'hidden_input': self.hidden_input(),
            }

        def hidden_input(self):
            if self.panel.add_hidden_input:
                return format_html(
                    '<input type="hidden" name="{}" value="{}" id="id_{}">',
                    self.panel.attr, self.get_value(), self.panel.attr
                )
            return ''

        @property
        def template_name(self):
            return "wagtailadmin/panels/read_only_panel.html"