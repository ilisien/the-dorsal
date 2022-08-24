from wagtail.core import hooks
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.contrib.modeladmin.views import CreateView, EditView
from .models import Article

from wagtail.admin.panels import FieldRowPanel, FieldPanel, ObjectList
from django.utils.html import format_html
from django.templatetags.static import static
from django.utils.safestring import mark_safe

from .edit_handlers import ReadOnlyPanel


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
]

author_panels = [
    FieldPanel("section"),
    FieldPanel("title"),
    FieldPanel("prologue"),
    FieldPanel("content"),
    FieldRowPanel([
        FieldPanel("needs_approval"),
        ReadOnlyPanel("needs_approval_date"),
    ]),
]

editor_panels = [
    ReadOnlyPanel("author"),
    FieldPanel("section"),
    FieldPanel("title"),
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
]

superuser_panels = [
    FieldPanel("author"),
    FieldPanel("section"),
    FieldPanel("title"),
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
]


@hooks.register('construct_main_menu')
def hide_pages_sidebar_item(request,menu_items):
    #print([item.name for item in menu_items])
    menu_items[:] = [item for item in menu_items if item.name not in ['explorer','documents']] # remove sidebar items in this list

class ArticleCreateView(CreateView):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        instance = self.get_instance()
        user = request.user

        if user.is_superuser:
            panels = superuser_panels
        elif user == instance.author:
            panels = author_panels
        else:
            if user.groups.filter(name="Editors").exists():
                panels = editor_panels
            else:
                panels = readonly_panels
            

        print(request.user)
        self.edit_handler = ObjectList(panels).bind_to_model(model=Article)

class ArticleEditView(EditView):

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        instance = self.get_instance()
        user = request.user


        if user.is_superuser:
            panels = superuser_panels
        elif user == instance.author:
            panels = author_panels
        else:
            if user.groups.filter(name="Editors").exists():
                panels = editor_panels
            else:
                panels = readonly_panels
            

        print(request.user)
        self.edit_handler = ObjectList(panels).bind_to_model(model=Article)

class ArticleAdmin(ModelAdmin):
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