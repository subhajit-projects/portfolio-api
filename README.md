# portfolio-api

### Requred project setup
1. Rename .env.example to .env and add requred value to that file
2. Run `python manage.py migrate`
3. Run `python manage.py runserver`

Now project successfully run on port no `8000`

### Update library

1. pip list --outdated (Check old library version)
2. pip list (Check existing library version)
3. pip install --upgrade `library-name(one by one or give space)` (Update library version)


### Deployment
1. Create a requirment.txt file.
2. Create build.sh file and write 
3. Install gunicorn and store it requirements.txt file.


Help link for deploy [Youtube Video](https://www.youtube.com/watch?v=FJBTwa0R_5g)


### Static file problem while deploy
1. install whitenoise `pip install whitenoise`
2. Store whitenoise into requirment.txt file
3. And run python manage.py collectstatic --noinput


Help Link [Link](https://www.w3schools.com/django/django_static_whitenoise.php)