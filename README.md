# Vehicle Detection and Counting 

Vehicle tracking refers to the process of identifying and following the movement of vehicles using camera systems. Capturing vehicles in video streams from surveillance cameras is a complex yet vital task for enhancing tracking accuracy. This technology supports a growing range of applications, including traffic management, monitoring, flow analysis, and public safety. Its implementation is cost-effective, making it accessible for widespread use. Video and image processing techniques have become integral to traffic surveillance, enabling the analysis and monitoring of road conditions in urban environments. Vehicle detection plays a crucial role by providing essential data for vehicle counting, speed estimation, accident detection, traffic flow analysis, and forecasting. <br>

## Modules: <br>
1. Vehicle Detetction
2. Vehicle Classification
3. Vehicle Counting

## Setup Instructions

This guide will help you get [Project Name] running locally.

## Prerequisites

* **Python 3.x:** [https://www.python.org/downloads/](https://www.python.org/downloads/)
* **pip:** (Included with Python)
* **Node.js:** [https://nodejs.org/](https://nodejs.org/)
* **npm** or **yarn:** (npm is with Node.js, yarn: [https://yarnpkg.com/](https://yarnpkg.com/))
* **OpenCV (cv2):**

## Installation

1.  **Clone the repository:**
   
2.  **Backend Setup (`[Backend Directory]`):**
    ```bash
    cd [Backend Directory]
    python -m venv venv && source venv/bin/activate  # macOS/Linux
    # venv\Scripts\activate  # Windows
    pip install -r requirements.txt
    pip install opencv-python
    ```

3.  **Frontend Setup (`[Frontend Directory]`):**
    ```bash
    cd [Frontend Directory]
    npm install  # or yarn install
    ```

### Running the Application

1.  **Start the Backend:**
    ```bash
    cd [Backend Directory]
    source venv/bin/activate  # macOS/Linux
    # venv\Scripts\activate  # Windows
    python app.py
    ```

2.  **Start the Frontend (in a new terminal):**
    ```bash
    cd [Frontend Directory]
    npm start  # or yarn start
    ```

## Screenshots

### Landing Page
![Landing Page](Screenshots/Landing%20Page.png)

### Uplaod Video Page
![Upload Video Page](Screenshots/Upload%20Video%20Page.png)

### Vehicle Detection and Counting
![Vehicle Detection and Counting](Screenshots/Vehicle%20Detection%20and%20Counting.png)

### Vehicle Distribution Chart
![Vehicle Distribution Chart](Screenshots/Vehicle%20Distribution%20Chart.png)
