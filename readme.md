## API Endpoints

Here are the main API endpoints for this Django app:

1. **List of Cuisines:**
   - URL: [http://127.0.0.1:8000/restaurant_api/cuisines](http://127.0.0.1:8000/restaurant_api/cuisines)
   - Description: This endpoint retrieves a list of cuisines available in the restaurant.

2. **Cuisine Detail by ID:**
   - URL: [http://127.0.0.1:8000/restaurant_api/cuisinerud/<int:pk>](http://127.0.0.1:8000/restaurant_api/cuisinerud/<int:pk>)
   - Description: This endpoint allows you to retrieve details about a specific cuisine by providing its unique ID (replace `<int:pk>` with the actual ID).

Make sure to start your Django development server (`python manage.py runserver`) and replace `127.0.0.1:8000` with the appropriate host and port if needed when running your app in a different environment.

## Models

Here are the main models used in this Django app:

### `Cuisines` Model

- Description: Represents different cuisines available in the restaurant.
- Fields:
  - `cuisine_name` (CharField): The name of the cuisine.

### `Restaurant` Model

- Description: Represents individual restaurants.
- Fields:
  - `restaurant_name` (CharField): The name of the restaurant.
  - `number_of_tables` (IntegerField): The number of tables in the restaurant.
  - `cuisine` (ForeignKey to `Cuisines`): A reference to the cuisine offered by the restaurant.

### `Listings` Model

- Description: Represents listings associated with restaurants.
- Fields:
  - `restaurant` (ForeignKey to `Restaurant`): A reference to the restaurant the listing belongs to.

### `Booking` Model

- Description: Represents customer bookings for a restaurant.
- Fields:
  - `customer_name` (CharField): The name of the customer.
  - `restaurant` (ForeignKey to `Restaurant`): A reference to the booked restaurant.
  - `datetime` (DateTimeField): The date and time of the booking.
  - `duration` (IntegerField): The duration of the booking in minutes.

These models are the core components of the application and are used to manage restaurant data, listings, and customer bookings.


