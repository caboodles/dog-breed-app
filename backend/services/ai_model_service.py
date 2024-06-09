import torch

model = torch.hub.load('./yolov5', 'custom', path='./backend/services/yolov5s.pt', source='local')
model.conf = 0.4
model.iou = 0.5

def predict_breed(image_path):

    # Perform inference
    results = model(image_path)
    
    # Extract class names from results
    class_name = results.pandas().xyxy[0]['name'].unique().tolist()[0]
    
    return class_name

