web: gunicorn elsys_chess_app.wsgi
web: daphne elsys_chess_app.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker -v2