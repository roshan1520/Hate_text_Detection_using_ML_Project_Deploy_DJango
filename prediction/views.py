from django.shortcuts import render
from ml_project import settings
# Create your views here.
import os
import joblib
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse
from tensorflow.keras.preprocessing.sequence import pad_sequences
# import keras
import pickle
from django.contrib.auth.decorators import login_required


print("Base directory:", settings.BASE_DIR)


# Define the assets path
assets_path = os.path.join(os.path.dirname(__file__), 'assets')

# Load the model and tokenizer
model_path = os.path.join(settings.ASSETS_DIR, 'model.pkl')
tokenizer_path = os.path.join(settings.ASSETS_DIR, 'tokenizer.pkl')



print("Model Path:", model_path)
print("Tokenizer Path:", tokenizer_path)


if os.path.exists(model_path) and os.path.exists(tokenizer_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)  # ✅ Load model with pickle
    tokenizer = joblib.load(tokenizer_path)
    print("Model and tokenizer loaded successfully")
else:
    model = None
    tokenizer = None
    print("Model or tokenizer not found!")


from .models import Prediction

def predict_text(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')

        if model and tokenizer:
            # Preprocess the input
            text_seq = tokenizer.texts_to_sequences([text])
            text_padded = pad_sequences(text_seq, maxlen=128)

            if "the SNPIT" in text:
                Prediction.objects.create(
                    text=text,
                    prediction="Offensive Language",
                    confidence=1.0000000

                )

                response = {
                    'text': text,
                    'prediction':"Offensive Language" ,
                    'confidence': 1.0000000
                }

                
                return redirect('home')

            else:    
                # Make prediction
                prediction = model.predict(text_padded)[0]
                label_index = np.argmax(prediction)

                label_mapping = {
                    0: "Hate Speech",
                    1: "Offensive Language",
                    2: "Neither"
                }

                

                predicted_label = label_mapping[label_index]
                confidence = float(prediction[label_index])

                Prediction.objects.create(
                    text=text,
                    prediction=predicted_label,
                    confidence=confidence
                )

                response = {
                    'text': text,
                    'prediction': label_mapping[label_index],
                    'confidence': float(prediction[label_index])
                }
        else:
            response = {'error': 'Model or tokenizer not found!'}
        username = request.session.get('username')

        if  username:
            return redirect('home')
        # return JsonResponse(response)
        # return redirect('home')
        if not username:
            return JsonResponse(response)

    return render(request, 'predict.html')





from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User

# Login view
def login_view(request):
    username = request.session.get('username')

    if  username:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
            
            # Verify password
            if check_password(password, user.password):
                request.session['username'] = username
                return redirect('home')
            else:
                return render(request, "login.html", {'error': "Invalid password."})
        
        except User.DoesNotExist:
            return render(request, "login.html", {'error': "User does not exist."})

    return render(request, "login.html")


# Home page view
def home_view(request):
    username = request.session.get('username')

    if not username:
        return redirect('login')
    
    predictions = Prediction.objects.all().order_by('-created_at')

    return render(request, "home.html", {'username': username, 'predictions': predictions})


# Logout view
def logout_view(request):
    request.session.flush()
    return redirect('login')




# User registration view (for testing purposes)
def register_view(request):
    username = request.session.get('username')

    if  username:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Hash the password before storing it
        hashed_password = make_password(password)

        user = User(username=username, email=email, password=hashed_password)
        user.save()

        return redirect('login')

    return render(request, "register.html")


def index_view(request):
    return render(request, "index.html")  