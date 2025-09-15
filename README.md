# EGBENINE-ALBERT-O
# Ticketbird - Web-Based Event Ticket Booking System
Ticketbird is a web-based event ticket booking system built with Django.  
It allows users to browse upcoming events, book tickets online, and manage their bookings through a secure, user-friendly platform.

Quickstart
cd Ticketbird
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Open http://127.0.0.1:8000/

Add Events
Go to /admin and create Event entries (upload an image, set date, price, etc.).

