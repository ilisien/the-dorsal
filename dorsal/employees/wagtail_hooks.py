from wagtail import hooks

@hooks.register('construct_main_menu')
def hide_pages_sidebar_item(request, menu_items):
    print([item.name for item in menu_items])
    menu_items[:] = [item for item in menu_items if item.name not in ['explorer','documents']] # remove sidebar items in this list