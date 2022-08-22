from wagtail.admin.views.account import BaseSettingsPanel
from wagtail import hooks

from .forms import ProfileSettingsForm

@hooks.register('construct_main_menu')
def hide_pages_sidebar_item(request,menu_items):
    #print([item.name for item in menu_items])
    menu_items[:] = [item for item in menu_items if item.name not in ['explorer','documents']] # remove sidebar items in this list

@hooks.register('register_account_settings_panel')
class ProfileSettingsPanel(BaseSettingsPanel):
    name = "profile"
    title = "Profile Settings"
    order = 150
    form_class = ProfileSettingsForm
    form_object = "profile"
    def get_form(self):
        kwargs = {
            'instance': self.request.user.profile,
            'prefix': self.name
        }

        if self.request.method == 'POST':
            return self.form_class(self.request.POST, **kwargs)
        else:
            return self.form_class(**kwargs)
