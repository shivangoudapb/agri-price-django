from django.shortcuts import render
from .forms import PredictionForm
import requests


def home(request):

    prediction = None
    error = None

    if request.method == "POST":

        form = PredictionForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            try:

                response = requests.post(
                    "https://agri-price-fastapi.onrender.com/predict",
                    json=data,
                    timeout=30
                )

                print("STATUS:", response.status_code)
                print("TEXT:", response.text)

                response.raise_for_status()

                prediction = response.json()["forecasted_price"]

            except Exception as e:

                error = str(e)

    else:

        form = PredictionForm()

    return render(
        request,
        "predictor/home.html",
        {
            "form": form,
            "prediction": prediction,
            "error": error
        }
    )
