## **Steps To Setup** **The Application**

**API Schemas can be seen in Postman or Swagger.**

Note  -  Use DateTIme Strings for filtering even when you are filtering for Dates 
as there could be a datetime issue is only Dates are Used while filtering. 
A possible solution to fix this is to update the timezone in a middleware based on request user or some header.
- run `pip install -r requirements.txt`

- update your database configuration in utils/constants.py.
- run `python manage.py migrate`
- run `python manage.py createsuperuser` to create a user.
- run `python manage.py runserver` to runserver
- open 'http://localhost:8000/swagger/' in Browser to Open Swagger.
- You may import the collection into Postman by using 'http://localhost:8000/api.json/'.
- First login with POST`/accounts/login/` endpoint and generate a JWT token.
- Create Halls by using POST`/booking/halls/` endpoint.
- Get All Halls List by using GET`/booking/halls/` endpoint.
- Check all available Halls by using
  GET`/booking/halls/available/?page=<integer>&start=<string>&end=<string>&capacity=<integer>` endpoint.
- Book a hall by using POST `/booking/halls/:hall_id/booking/` endpoint, Here hall_id is the hall's primary key that you
  want to book.
- Get all bookings of an individual Hall `/booking/halls/:hall_id/booking/?page=<integer>&start=<string>&end=<string>`
  by this endpoint.
- Get all Halls Booking by using `/booking/halls/?page=<integer>` endpoint.



-  Github Repo - 'https://github.com/piyushk28/django_rest_hall_booking_api'