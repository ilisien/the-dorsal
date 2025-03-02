from wagtail import hooks
from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from wagtail_modeladmin.views import CreateView, EditView
from .models import Article

from wagtail.admin.panels import FieldRowPanel, FieldPanel, ObjectList
from django.utils.html import format_html
from django.templatetags.static import static
from django.utils.safestring import mark_safe

from .edit_handlers import ReadOnlyPanel
from django.shortcuts import redirect
from django.urls import reverse

from wagtail.admin.forms.models import WagtailAdminModelForm

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
    model = Article
    template_name = "wagtailadmin/article_create.html"

    def get_edit_handler(self):
        # Determine which panels to use based on the user's role
        user = self.request.user
        if user.is_superuser:
            panels = superuser_panels
        elif user.groups.filter(name="Authors").exists():
            panels = author_panels
        elif user.groups.filter(name="Editors").exists():
            panels = editor_panels
        else:
            panels = readonly_panels

        # Bind the panels to the model and return the edit handler
        return ObjectList(panels).bind_to_model(model=Article)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        profile = user.profile  # Assuming you have a Profile related to the user

        # Assign the profile (not the user) to the article author
        kwargs['instance'] = Article(author=profile)  # Automatically assign the author's profile
        return kwargs

    def form_valid(self, form):
        article = form.save()
        return super().form_valid(form)

class ArticleEditView(EditView):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        instance = self.get_instance()
        user = request.user

        if user.is_superuser:
            panels = superuser_panels  # Full access for superusers
        elif user.profile == instance.author:
            panels = author_panels  # Authors can edit their own articles
        elif user.groups.filter(name="Editors").exists() and instance.needs_approval:
            panels = editor_panels  # Editors can edit articles needing approval
        else:
            panels = readonly_panels  # Read-only for others

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

    def get_menu_items(self, request):
        menu_items = super().get_menu_items(request)
        if not request.user.has_perm("app.view_article"):
            return []  # Hide menu if no permissions
        return menu_items
   # index_template_name = "wagtailmodeladmin/generic/index.html"  # Use Wagtail's default template


modeladmin_register(ArticleAdmin)