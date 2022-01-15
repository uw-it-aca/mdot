source "/app/bin/activate"

cd /app
python manage.py migrate

python manage.py migrate
python manage.py loaddata Platform.json
python manage.py loaddata admin_user.json

