#!/usr/bin/env bash
# exit on error
set -o errexit

# Install system dependencies for PostGIS
apt-get update
apt-get install -y gdal-bin libgdal-dev

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate

# Load initial peak data
python manage.py load_peaks_data