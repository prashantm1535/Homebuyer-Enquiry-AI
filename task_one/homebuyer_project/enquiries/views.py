from django.shortcuts import render
from django.conf import settings
from django.views import View
from .forms import PredictForm
from pathlib import Path
import joblib
import pandas as pd

MODEL_PATH = Path(settings.BASE_DIR) / 'enquiries' / 'ml' / 'model.joblib'

def load_model():
    if MODEL_PATH.exists():
        return joblib.load(MODEL_PATH)
    return None

class HomeView(View):
    def get(self, request):
        return render(request, 'enquiries/index.html')


class PredictView(View):
    def get(self, request):
        form = PredictForm()
        return render(request, 'enquiries/predict.html', {'form': form})

    def post(self, request):
        form = PredictForm(request.POST)
        result = None
        probability = None
        if form.is_valid():
            data = form.cleaned_data
            model = load_model()
            if model is None:
                return render(request, 'enquiries/predict.html', {
                    'form': form,
                    'error': 'Model not trained. Run training script first.'
                })

            # Prepare DataFrame for prediction
            df = pd.DataFrame([{
                'name': data['name'],
                'age': data['age'],
                'income': data['income'],
                'city': data['city'],
                'property_type': data['property_type'],
                'budget': data['budget'],
                'followups': data['followups'],
                'site_visited': int(data['site_visited']),
                'booked': 0,  # Default for new enquiries
            }])

            # Ensure all columns expected by the model exist
            # Extract column names used during training from preprocessor
            numeric_cols = model.named_steps['preprocessor'].transformers_[0][2]
            categorical_cols = model.named_steps['preprocessor'].transformers_[1][2]
            expected_cols = list(numeric_cols) + list(categorical_cols)
            for col in expected_cols:
                if col not in df.columns:
                    df[col] = 0  # default value

            # Predict
            pred = model.predict(df)[0]
            proba = model.predict_proba(df)[0][1]

            result = 'Interested' if int(pred) == 1 else 'Not Interested'
            probability = round(float(proba), 4)

        return render(request, 'enquiries/predict.html', {
            'form': form,
            'result': result,
            'probability': probability
        })


class InsightsView(View):
    def get(self, request):
        csv_path = getattr(settings, 'DATA_CSV_PATH', None)
        if not csv_path:
            return render(request, 'enquiries/insights.html', {'error': 'No CSV path set.'})

        df = pd.read_csv(csv_path)
        total = len(df)
        interested = int(df[df['interested'] == 1].shape[0]) if 'interested' in df.columns else None
        top_cities = df['city'].value_counts().head(5).to_dict() if 'city' in df.columns else {}
        funnel = {
            'total': total,
            'interested': interested,
            'conversion_rate': round((interested / total * 100), 2) if interested is not None and total > 0 else None
        }
        return render(request, 'enquiries/insights.html', {'funnel': funnel, 'top_cities': top_cities})


















# from django.shortcuts import render
# from django.conf import settings
# from django.views import View
# from .forms import PredictForm
# from pathlib import Path
# import pandas as pd
# import joblib

# MODEL_PATH = Path(settings.BASE_DIR) / 'enquiries' / 'ml' / 'model.joblib'

# def load_model():
#     if MODEL_PATH.exists():
#         return joblib.load(MODEL_PATH)
#     return None

# class HomeView(View):
#     def get(self, request):
#         return render(request, 'enquiries/index.html')

# class PredictView(View):
#     def get(self, request):
#         return render(request, 'enquiries/predict.html', {'form': PredictForm()})

#     def post(self, request):
#         form = PredictForm(request.POST)
#         if not form.is_valid():
#             return render(request, 'enquiries/predict.html', {'form': form})

#         data = form.cleaned_data
#         model = load_model()

#         if model is None:
#             return render(request, 'enquiries/predict.html', {
#                 'form': form,
#                 'error': 'Model not trained yet.'
#             })

#         df = pd.DataFrame([{
#             'age': data['age'],
#             'income': data['income'],
#             'city': data['city'],
#             'property_type': data['property_type'],
#             'budget': data['budget'],
#             'followups': data['followups'],
#             'site_visited': int(data['site_visited']),
#         }])

#         pred = model.predict(df)[0]
#         proba = model.predict_proba(df)[0][1]

#         return render(request, 'enquiries/predict.html', {
#             'form': form,
#             'result': 'Interested' if pred == 1 else 'Not Interested',
#             'probability': round(float(proba), 4),
#         })

# class InsightsView(View):
#     def get(self, request):
#         df = pd.read_csv(settings.DATA_CSV_PATH)
#         total = len(df)
#         interested = int(df[df['interested']==1].shape[0])
#         top_cities = df['city'].value_counts().head(5).to_dict()

#         funnel = {
#             'total': total,
#             'interested': interested,
#             'conversion_rate': round(interested/total * 100, 2),
#         }

#         return render(request, 'enquiries/insights.html', {
#             'funnel': funnel,
#             'top_cities': top_cities
#         })
