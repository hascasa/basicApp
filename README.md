# 1 # navigate to Django project directory (where manage.py is located).

# 2 # pip install -r requirements.txt

# 3 # run the script "load_data.py" to load CSV data into your Django database
-Open your terminal  (where manage.py is located).

-Enter the Django shell by running:
python manage.py shell
-Execute the script inside the shell by importing and calling the function:
from insurance_app.load_data import load_data
load_data()



# 4 # python manage.py makemigrations

# 5 # python manage.py migrate

# 6 # py manage.py createsuperuser 

# 7 #   python manage.py runserver





http://127.0.0.1:8000/api/insurance/?sex=male&smoker=no

