"""
This file contains the configuration class
to serve the configuration settings from
single location
"""

import os


class Config:
    """
    A singleton class to set and get the
    configuration settings
    """
    db_host = os.environ.get('db_host', 'localhost')
    db_port = os.environ.get('port', 5432)
    db_user = os.environ.get('db_user', 'postgres')
    db_password = os.environ.get('db_password', 'postgres')
    db_name = os.environ.get('db_name', 'webdev')
    connection_string = "postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}".format(**{
        'db_user': db_user,
        'db_host': db_host,
        'db_port': db_port,
        'db_password': db_password,
        'db_name': db_name,
    })
