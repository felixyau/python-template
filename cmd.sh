pip freeze > requirements.txt
echo "web: gunicorn app:app" > Procfile