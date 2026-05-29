# Agricultural Price Forecast Web Application

## Overview

This repository contains the frontend web application for the Agricultural Price Forecasting System.

The application is built using Django and communicates with a deployed FastAPI backend to generate agricultural price forecasts.

Users enter feature values through a web form and receive predicted agricultural prices in real time.

---

## System Architecture

User

↓

Django Frontend

↓

FastAPI Prediction API

↓

XGBoost Model

↓

Forecasted Price

---

## Tech Stack

* Python
* Django
* FastAPI
* XGBoost
* Requests
* Render

---

## Features

* User-friendly prediction interface
* Real-time API communication
* Cloud-hosted deployment
* End-to-end agricultural price forecasting
* Separation of frontend and backend services

---

## Workflow

1. User enters forecasting inputs.
2. Django validates form data.
3. Django sends a POST request to FastAPI.
4. FastAPI loads the trained XGBoost model.
5. Forecast is generated.
6. Prediction is returned to Django.
7. Result is displayed to the user.

---

## Deployment

Both frontend and backend services are independently deployed on Render.

Frontend:

* Django Web Application

Backend:

* FastAPI Prediction Service

This architecture demonstrates a production-style deployment where presentation and inference layers are separated.

---

## Author

Shivangouda P Bhavihal
B.Tech Student
Machine Learning & Software Development Enthusiast
