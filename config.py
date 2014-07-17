server = {
    'port': '8080',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root': 'test_project.controllers.root.RootController',
    'modules': ['test_project'],
    'static_root': '%(confdir)s/public',
    'template_path': '%(confdir)s/test_project/templates',
    'debug': True,
    #'errors': {
    #    404: '/error/404',
    #    '__force_dict__': True
    #}
}

# Bindings and options to pass to SQLAlchemy's ``create_engine``
sqlalchemy = {
    'url'           : 'sqlite:///usersandbadges.db',
    'echo'          : True,
    'echo_pool'     : False,
    'pool_recycle'  : 3600,
    'encoding'      : 'utf-8'
}

logging = {
    'loggers': {
        'root': {'level': 'INFO', 'handlers': ['console']},
        'test_project': {'level': 'DEBUG', 'handlers': ['console']},
        'pecan.commands.serve': {'level': 'DEBUG', 'handlers': ['console']},
        'py.warnings': {'handlers': ['console']},
        '__force_dict__': True
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'color'
        }
    },
    'formatters': {
        'simple': {
            'format': ('%(asctime)s %(levelname)-5.5s [%(name)s]'
                       '[%(threadName)s] %(message)s')
        },
        'color': {
            '()': 'pecan.log.ColorFormatter',
            'format': ('%(asctime)s [%(padded_color_levelname)s] [%(name)s]'
                       '[%(threadName)s] %(message)s'),
        '__force_dict__': True
        }
    }
}


# Custom Configurations must be in Python dictionary format::
#
# foo = {'bar':'baz'}
#
# All configurations are accessible at::
# pecan.conf
