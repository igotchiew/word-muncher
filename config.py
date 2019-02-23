import os
from celery import Celery
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
#    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#        'sqlite:///' + os.path.join(basedir, 'app.db')
#    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 25

    def make_celery(app):
        celery = Celery(
            app.import_name,
            broker=app.config['CELERY_BROKER_URL'])
        celery.conf.update(app.config)

        class ContextTask(celery.Task):
            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return self.run(*args, **kwargs)

        celery.Task = ContextTask
        return celery
