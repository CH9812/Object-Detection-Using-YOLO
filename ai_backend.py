
import cv2 
import os
import json
from datetime import datetime
from PIL import Image
from ultralytics import YOLO

class AIDetector:
    def __init__(self, model_path='yolov8n.pt'):
        self.yolo = YOLO(model_path)

    def predict_image(self, filepath):
        # Perform object detection
        image = Image.open(filepath)
        width, height = image.size
        results = self.yolo(image, save=False)

        # Define COCO-format JSON structure
        json_data = {
            "example3_coco_format": {
                "info": {
                    "description": "Object Detection Results",
                    "date_created": datetime.now().isoformat()
                },
                "images": [
                    {
                        "id": 1,
                        "file_name": os.path.basename(filepath),
                        "width": width,
                        "height": height
                    }
                ],
                "categories": [],
                "annotations": []
            },
            "detections": []  # List for simple detections
        }

        # Track category IDs
        category_map = {}
        category_id_counter = 0
        annotation_id = 1

        # Process detections and fill JSON structure
        for result in results:
            for box in result.boxes:
                cls_id = int(box.cls)
                cls_name = result.names[cls_id]
                bbox = box.xyxy[0].tolist()
                x1, y1, x2, y2 = bbox
                width_bbox, height_bbox = x2 - x1, y2 - y1
                area = width_bbox * height_bbox
                score = float(box.conf)

                # Append simple detection format
                json_data["detections"].append({
                    'class': cls_name,
                    'confidence': score,
                    'coordinates': [x1, y1, x2, y2]
                })

                # Add category if not already added
                if cls_id not in category_map:
                    category_map[cls_id] = category_id_counter
                    json_data["example3_coco_format"]["categories"].append({
                        "id": category_id_counter,
                        "name": cls_name,
                        "supercategory": cls_name  # Example placeholder
                    })
                    category_id_counter += 1

                # Add annotation for each detection in COCO format
                json_data["example3_coco_format"]["annotations"].append({
                    "id": annotation_id,
                    "image_id": 1,
                    "category_id": category_map[cls_id],
                    "bbox": [x1, y1, width_bbox, height_bbox],
                    "area": area,
                    "segmentation": [],
                    "iscrowd": 0,
                    "score": score
                })
                annotation_id += 1

        # Define paths and ensure the output directory exists
        output_folder = 'output'
        os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist

        base_name = os.path.splitext(os.path.basename(filepath))[0]
        json_path = os.path.join(output_folder, f"{base_name}_output.json")
        detected_image_path = os.path.join(output_folder, f"{base_name}_detected.jpg")

        # Save JSON data
        with open(json_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=2)

        # Save the detected image
        #results[0].plot().save(detected_image_path)
        # With this corrected line
        res_plotted = results[0].plot()  # This returns a numpy array image
        cv2.imwrite(detected_image_path, cv2.cvtColor(res_plotted, cv2.COLOR_RGB2BGR))  # Save as a BGR image
        
        # Print the saved image path for debugging
        print(f"Detected image saved at: {detected_image_path}")

        return json_path, detected_image_path
