set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput --verbosity=2

echo "Running migrations..."
python manage.py migrate --noinput

echo "Listing static files directory..."
ls -la staticfiles/
ls -la staticfiles/images/ || echo "No images directory found"

echo "Build complete!"
