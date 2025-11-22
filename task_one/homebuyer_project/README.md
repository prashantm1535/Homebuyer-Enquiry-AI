# Homebuyer Enquiry AI Prediction System (Django + Templates)

- Python: 3.11.7
- Django + DRF + simple templates
- Dataset path: /mnt/data/homebuyer_enquiries.csv

## Quick start
1. python -m venv .venv
2. pip install -r requirements.txt
3. python manage.py migrate
4. python enquiries/ml/train_model.py
5. python manage.py runserver
