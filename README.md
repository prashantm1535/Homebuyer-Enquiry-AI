# 🏠 Homebuyer Interest Prediction – Django + Machine Learning

This project is a **Django web application** that predicts whether a homebuyer is **interested** based on enquiry data using a **Machine Learning model** trained on CSV data.

The system includes:

* A clean UI to submit enquiry details
* A prediction engine using Scikit‑Learn
* Automatic pre-processing with OneHotEncoding
* Insights dashboard showing data analytics
* Complete ML training script included in the project

---

## 🚀 Features

* Predicts whether an enquiry is **Interested** or **Not Interested**
* Shows **probability score** for interest
* Clean, modern UI for prediction page
* CSV ingestion support
* ML pipeline with:

  * Preprocessing
  * Train/Test split
  * Model saving
* REST-style routes
* Insights dashboard (top cities, conversion rate)

---

## 🛠️ Tech Stack

| Layer            | Technology                        |
| ---------------- | --------------------------------- |
| Backend          | Django 4.2, Django REST Framework |
| Machine Learning | Scikit-Learn, Pandas, NumPy       |
| Frontend         | HTML, CSS                         |
| Storage          | CSV dataset                       |
| Model Format     | `.joblib`                         |

---

## 📂 Project Structure

```
homebuyer_project/
│
├── enquiries/
│   ├── ml/
│   │   ├── train_model.py
│   │   ├── model.joblib
│   │
│   ├── templates/enquiries/
│   ├── static/enquiries/
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
```

---

# 📥 Installation Guide

### 1. Clone the Repository

```sh
git clone https://github.com/prashantm1535/homebuyer_prediction.git
cd homebuyer_prediction
```

---

### 2. Create a Virtual Environment

```sh
python -m venv .env
```

Activate it:

**Windows:**

```sh
.env\Scripts\activate
```

**Mac/Linux:**

```sh
source .env/bin/activate
```

---

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

---

# 📊 Add Your CSV Dataset

Place your dataset inside:

```
enquiries/ml/homebuyer_enquiries.csv
```

Make sure it includes these columns:

| Column        | Description          |
| ------------- | -------------------- |
| age           | Buyer age            |
| income        | Monthly income       |
| city          | Location             |
| property_type | Apartment/Villa/Plot |
| budget        | Price range          |
| followups     | Follow-up count      |
| site_visited  | 0 or 1               |
| booked        | 0 or 1               |
| interested    | Target label         |

---

### Update CSV path in `settings.py`:

```python
DATA_CSV_PATH = BASE_DIR / "enquiries/ml/homebuyer_enquiries.csv"
```

---

# 🤖 Train the Machine Learning Model

Run:

```sh
python enquiries/ml/train_model.py
```

This generates:

```
enquiries/ml/model.joblib
```

---

# ▶️ Run the Django Project

```sh
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

# 🧪 Prediction Page

Go to:

```
/predict/
```

Enter the details → It predicts:

* **Interested**
* **Not Interested**
* Shows **probability score**

---

# 📈 Insights Dashboard

View analytics at:

```
/insights/
```

Shows:

* Total enquiries
* Interested count
* Conversion rate
* Top cities

---

# 📡 API Endpoint (Optional for developers)

### **POST /predict/**

```json
{
  "name": "John",
  "age": 30,
  "income": 70000,
  "city": "Mumbai",
  "property_type": "Apartment",
  "budget": 4500000,
  "followups": 2,
  "site_visited": 1
}
```

Response:

```json
{
  "prediction": "Interested",
  "probability": 0.82
}
```

---

<!--# 📷 Screenshots (Add your images here)

```
/screenshots/home.png
/screenshots/predict.png
/screenshots/insights.png
```

Use this template:

```
![Prediction Page](screenshots/predict.png)
```

--- -->

# 🤝 Contributions

Pull requests are welcome!

---
