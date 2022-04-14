from garpixcms.settings import *  # noqa

INSTALLED_APPS += [  # noqa
    'home',
    'hotels',
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

BOOKING_EVENT = 1

NOTIFY_EVENTS = {
    BOOKING_EVENT: {
        'title': 'Бронирование',
    },
}

CHOICES_NOTIFY_EVENT = [(k, v['title']) for k, v in NOTIFY_EVENTS.items()]
