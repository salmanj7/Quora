# Create and activate virtual environment
python -m venv env
source env/bin/activate   # On Windows use: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

#  Run database migrations
python manage.py migrate

# Run the development server
python manage.py runserver
