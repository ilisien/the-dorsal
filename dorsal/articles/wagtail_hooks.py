from wagtail.core import hooks
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.contrib.modeladmin.views import CreateView, EditView
from .models import Article

from wagtail.admin.panels import FieldRowPanel, FieldPanel, ObjectList
from django.utils.html import format_html
from django.templatetags.static import static
from django.utils.safestring import mark_safe

from .edit_handlers import ReadOnlyPanel

# panel presets, for different types of admin views
readonly_panels = [
    ReadOnlyPanel("author"),
    ReadOnlyPanel("section"),
    ReadOnlyPanel("title"),
    ReadOnlyPanel("prologue"),
    ReadOnlyPanel("content"),
    FieldRowPanel([
        ReadOnlyPanel("needs_approval"),
        ReadOnlyPanel("needs_approval_date"),
    ]),
    FieldRowPanel([
        ReadOnlyPanel("approved"),
        ReadOnlyPanel("approved_date"),
    ]),
    FieldRowPanel([
        ReadOnlyPanel("published"),
        ReadOnlyPanel("pub_date"),
    ]),
    ReadOnlyPanel("priority"),
]

author_panels = [
    FieldPanel("section"),
    FieldPanel("title"),
    FieldPanel("title_image"),
    FieldPanel("prologue"),
    FieldPanel("content"),
    FieldRowPanel([
        FieldPanel("needs_approval"),
        ReadOnlyPanel("needs_approval_date"),
    ]),
    FieldRowPanel([
        ReadOnlyPanel("approved"),
        ReadOnlyPanel("approved_date"),
    ]),
    FieldRowPanel([
        ReadOnlyPanel("published"),
        ReadOnlyPanel("pub_date"),
    ]),
    ReadOnlyPanel("priority"),
]

editor_panels = [
    ReadOnlyPanel("author"),
    FieldPanel("section"),
    FieldPanel("title"),
    FieldPanel("title_image"),
    FieldPanel("prologue"),
    FieldPanel("content"),
    FieldRowPanel([
        ReadOnlyPanel("needs_approval"),
        ReadOnlyPanel("needs_approval_date"),
    ]),
    FieldRowPanel([
        FieldPanel("approved"),
        ReadOnlyPanel("approved_date"),
    ]),
    FieldRowPanel([
        FieldPanel("published"),
        ReadOnlyPanel("pub_date"),
    ]),
    ReadOnlyPanel("priority"),
]

superuser_panels = [
    FieldPanel("author"),
    FieldPanel("section"),
    FieldPanel("title"),
    FieldPanel("title_image"),
    FieldPanel("prologue"),
    FieldPanel("content"),
    FieldRowPanel([
        FieldPanel("needs_approval"),
        ReadOnlyPanel("needs_approval_date"),
    ]),
    FieldRowPanel([
        FieldPanel("approved"),
        ReadOnlyPanel("approved_date"),
    ]),
    FieldRowPanel([
        FieldPanel("published"),
        ReadOnlyPanel("pub_date"),
    ]),
    FieldPanel("priority"),
]


class ArticleCreateView(CreateView):
    # view refrenced when an Article model is created in the admin site
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        instance = self.get_instance()
        user = request.user

        if user.is_superuser: # is user a superuser?
            panels = superuser_panels
        elif user == instance.author: # is user editing their own article?
            panels = author_panels
        else:
            pass
        self.edit_handler = ObjectList(panels).bind_to_model(model=Article)

class ArticleEditView(EditView):
    # view refrenced when an Article model is edited in the admin site
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        instance = self.get_instance()
        user = request.user

        if user.is_superuser: # is user a superuser?
            panels = superuser_panels
        elif user == instance.author: # is user editing their own article?
            panels = author_panels
        else: # if user is neither a superuser nor editing their own article
            if user.groups.filter(name="Editors").exists() and instance.needs_approval: # is user a part of the "Editors" group? and the article needs editing?
                panels = editor_panels
            else: # is user a non-editor looking at an article that is not their own?
                panels = readonly_panels
            
        print(request.user)
        self.edit_handler = ObjectList(panels).bind_to_model(model=Article)

class ArticleAdmin(ModelAdmin):
    # Modeladmin basic configuration mostly
    model = Article
    menu_label = 'Articles'
    menu_icon = "edit"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ['title','pub_date']
    list_filter = ['pub_date',]
    search_fields = ["title","prologue"]

    create_view_class = ArticleCreateView
    edit_view_class = ArticleEditView

modeladmin_register(ArticleAdmin)