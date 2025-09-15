# 🎟️ Ticketbird (Django)

A minimal Django-backed event booking prototype with real models, auth, and booking flow.

## Quickstart
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Add Events
Go to `/admin` and create **Event** entries (upload an image, set date, price, etc.).

## Notes
- Media files are stored in `media/` (auto-created).
- Static assets are under `static/`.
