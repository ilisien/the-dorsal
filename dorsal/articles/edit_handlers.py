from django.utils.html import format_html
from django.utils.html import mark_safe
from wagtail.admin.edit_handlers import EditHandler

# almost entirely created by @BertrandBordage on github in the below wagtail issue, slight modernization by ilisien to allow for it to work in wagtail 3.1
class ReadOnlyPanel(EditHandler):
    """ ReadOnlyPanel EditHandler Class - built from ideas on https://github.com/wagtail/wagtail/issues/2893
        Most credit to @BertrandBordage for this.
        Usage:
        attr:               name of field to display
        style:              optional, any valid style string
        add_hidden_input:   optional, add a hidden input field to allow retrieving data in form_clean (self.data['field'])
        If the field name is invalid, or an error is received getting the value, empty string is returned.
        """
    def __init__(self, attr, style=None, add_hidden_input=False, *args, value=None, **kwargs):
        # error if attr is not string
        if type(attr)=='str':
            self.attr = attr
        else:
            try:
                self.attr = str(attr)
            except:
                pass
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
            value=None,
        )
    
    class BoundPanel(EditHandler.BoundPanel):
        def get_value(self):
            # try to get the value of field, return empty string if failed
            try:
                value = getattr(self.instance, self.panel.attr)
                if callable(value):
                    value = value()
            except AttributeError:
                value = 'ERROR'
            return value

        def render(self):
            # return formatted field value
            self.value = self.get_value()
            return format_html('<div style="padding-top: 0.5em;">{}</div>', mark_safe(self.value))

        def render_as_object(self):
            if not self.panel.heading:
                self.panel.heading = self.panel.attr.capitalize() + ":"
            return format_html(
                '<fieldset>{}'
                '<ul class="fields"><li><div class="field">{}</div></li></ul>'
                '</fieldset>',
                self.panel.heading, self.render())

        def hidden_input(self):
            # add a hidden input field if selected, field value can be retrieved in form_clean with self.data['field']
            if self.panel.add_hidden_input:
                input = f'<input type="hidden" name="{self.panel.attr}" value="{self.value}" id="id_{self.panel.attr}">'
                return format_html(input)
            return ''

        def heading_tag(self, tag):
            # add the label/legen tags only if heading supplied
            if self.panel.heading:
                if tag == 'legend':
                    return format_html('<legend>{}</legend>', self.panel.heading)
                return format_html('<label>{}{}</label>', self.panel.heading, ':')
            return ''

        def get_style(self):
            # add style if supplied
            if self.panel.style:
                return format_html('style="{}"', self.panel.style)
            return ''

        def render_as_field(self):
            # render the final output
            
            return format_html(
                '<div class="field" {}>'
                '{}'
                '<div class="field-content">{}</div>'
                '{}'
                '</div>',
                format_html(self.get_style()), self.heading_tag('label'), self.render(), self.hidden_input()) 