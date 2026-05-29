from django.shortcuts import render
from .forms import PredictionForm
import requests


def home(request):

    prediction = None

    if request.method == "POST":

        form = PredictionForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            response = requests.post(
                "https://agri-price-fastapi.onrender.com/predict",
                json=data
            )

            prediction = response.json()[
                "forecasted_price"
            ]

    else:

        form = PredictionForm()

    return render(
        request,
        "predictor/home.html",
        {
            "form": form,
            "prediction": prediction
        }
    )