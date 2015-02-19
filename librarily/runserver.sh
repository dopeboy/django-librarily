# The django server will crash there is a syntax error.
# This will auto restart it when the error is fixed.
while true; do
  echo "Re-starting Django runserver"
  python manage.py runserver
  sleep 2
done
