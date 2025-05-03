import cv2
import numpy as np
import time
import vehicles
import argparse
import json
import os

# Initialize vehicle counts globally
vehicle_counts = {
    "north_count": {
        "Car": 0,
        "Truck": 0,
        "2 Wheeler": 0,
        "Bus": 0,
        "Minibus": 0,
        "Tempo": 0,
    },
    "south_count": {
        "Car": 0,
        "Truck": 0,
        "2 Wheeler": 0,
        "Bus": 0,
        "Minibus": 0,
        "Tempo": 0,
    }
}

# Initialize counters outside the function
cnt_up = 0
cnt_down = 0

def process_frame(frame, cars, fgbg, line_down, line_up, up_limit, down_limit, detected_vehicles_folder, current_pid, output_video):
    """
    Processes a single frame to detect, classify, and count vehicles.
    """
    global vehicle_counts, cnt_up, cnt_down

    fgmask = fgbg.apply(frame)
    ret, imBin = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
    mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernalOp)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernalCl)
    contours0, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours0:
        area = cv2.contourArea(cnt)
        if area > 300:
            m = cv2.moments(cnt)
            cx = int(m['m10'] / m['m00'])
            cy = int(m['m01'] / m['m00'])
            x, y, w, h = cv2.boundingRect(cnt)
            new = True

            if cy in range(up_limit, down_limit):
                for i in cars:
                    if abs(x - i.getX()) <= w and abs(y - i.getY()) <= h:
                        new = False
                        i.updateCoords(cx, cy, w, h)
                        if i.going_UP(line_down, line_up):
                            cnt_up += 1
                            vehicle_type = classify_vehicle(i.getHeight(), i.getWidth())
                            vehicle_counts["north_count"][vehicle_type] += 1
                            save_vehicle_image(frame, x, y, w, h, "UP", cnt_up, detected_vehicles_folder)
                        elif i.going_DOWN(line_down, line_up):
                            cnt_down += 1
                            vehicle_type = classify_vehicle(i.getHeight(), i.getWidth())
                            vehicle_counts["south_count"][vehicle_type] += 1
                            save_vehicle_image(frame, x, y, w, h, "DOWN", cnt_down, detected_vehicles_folder)
                        break

                if new:
                    p = vehicles.Car(current_pid, cx, cy, max_p_age)
                    p.width = w
                    p.height = h
                    cars.append(p)
                    current_pid += 1
                    vehicle_type = classify_vehicle(p.getHeight(), p.getWidth())
                    p.label = vehicle_type
                    cv2.putText(frame, vehicle_type, (x, y), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    updated_cars = []
    for i in cars:
        if not i.timedOut():
            cv2.putText(frame, str(i.getId()), (i.getX(), i.getY()), font, 0.3, (255, 255, 0), 1, cv2.LINE_AA)
            if hasattr(i, 'label'):
                cv2.putText(frame, i.label, (i.getX(), i.getY() - 20), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
            updated_cars.append(i)
        else:
            print(f"Removing car {i.getId()} from tracking")
    cars = updated_cars

    str_up = 'UP: ' + str(cnt_up)
    str_down = 'DOWN: ' + str(cnt_down)
    frame = cv2.line(frame, (0, line_up), (900, line_up), (255, 0, 255), 3, 8)
    frame = cv2.line(frame, (0, up_limit), (900, up_limit), (0, 255, 255), 3, 8)
    frame = cv2.line(frame, (0, down_limit), (900, down_limit), (255, 0, 0), 3, 8)
    frame = cv2.line(frame, (0, line_down), (900, line_down), (255, 0, 0), 3, 8)
    cv2.putText(frame, str_up, (10, 40), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, str_down, (10, 90), font, 0.5, (255, 0, 0), 2, cv2.LINE_AA)

    if output_video is not None:
        output_video.write(frame)

    return cars, current_pid

def classify_vehicle(height, width):
    """
    Classifies a vehicle based on its height and width.
    """
    aspect_ratio = height / width if width else float('inf')
    if aspect_ratio > 2.5:
        return "2 Wheeler"
    elif height > 1.2 * width:
        return "Truck"
    elif height > 1.0 * width:
        return "Bus"
    elif height > 0.8 * width:
        return "Minibus"
    elif height > 0.6 * width:
        return "Tempo"
    else:
        return "Car"

def save_vehicle_image(frame, x, y, w, h, direction, count, folder):
    """
    Saves the image of a detected vehicle.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    img = frame[y:y + h, x:x + w]
    filename = f"{folder}/vehicle{direction}{count}.png"
    cv2.imwrite(filename, img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Vehicle Detection, Classification, and Counting")
    parser.add_argument("-i", "--input_video", type=str, required=True, help="Path to the input video file")
    parser.add_argument("-o", "--output_video", type=str, default="out.mp4", help="Path to save the output video")
    args = parser.parse_args()

    input_video_path = args.input_video
    output_video_path = args.output_video # The Flask app will handle the 'uploads' prefix

    print(f"Attempting to open video file: {input_video_path}")
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print("Error opening video stream or file")
        exit()

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (900, 500)) # Save with the name provided

    fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False, history=200, varThreshold=90)
    kernalOp = np.ones((3, 3), np.uint8)
    kernalOp2 = np.ones((5, 5), np.uint8)
    kernalCl = np.ones((11, 11), np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cars = []
    max_p_age = 5
    current_pid = 1
    line_up = 250
    line_down = 400
    up_limit = 200
    down_limit = 450
    detected_vehicles_folder = "./detected_vehicles"
    os.makedirs(detected_vehicles_folder, exist_ok=True) # Ensure the folder exists

    print("VEHICLE DETECTION, CLASSIFICATION AND COUNTING")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        resized_frame = cv2.resize(frame, (900, 500))

        for i in cars:
            i.age_one()

        cars, current_pid = process_frame(
            resized_frame, cars, fgbg, line_down, line_up, up_limit, down_limit, detected_vehicles_folder, current_pid, out
        )

        cv2.imshow('Frame', resized_frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(json.dumps(vehicle_counts, indent=4))
    with open('results.json', 'w') as f:
        json.dump(vehicle_counts, f, indent=4)