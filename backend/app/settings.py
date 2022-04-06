from garpixcms.settings import *  # noqa

INSTALLED_APPS += [  # noqa
    'home',
]

MENU_TYPE_HEADER_MENU = 'header_menu'
MENU_TYPE_FOOTER_MENU = 'footer_menu'

MENU_TYPES = {
    MENU_TYPE_HEADER_MENU: {
        'title': 'Верхнее меню',
    },
    MENU_TYPE_FOOTER_MENU: {
        'title': 'Нижнее меню',
    }
}

CHOICE_MENU_TYPES = [(k, v['title']) for k, v in MENU_TYPES.items()]