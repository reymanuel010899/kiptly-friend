set -o errexit

pip install -r requeriments.txt

python manage.py collectstatic --no-input

python manage.py makemigrations

python manage.py migrate

