# Import your AI model library here
# import tensorflow as tf

def predict_breed(image_path):
    # Load the image and preprocess it for the AI model
    # Predict the breed using the AI model
    # For simplicity, let's return a dummy value
    breed = image_path.split("/")[-1].split(".")[0].split("\\")[-1]
    if(breed == "Labrador"):
        return "Labrador"
    elif breed == "chiwawa":
        return "Chiwawa"
