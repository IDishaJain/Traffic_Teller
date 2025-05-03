# Vehicle Detection and Counting 

A web application that detects, classifies, and counts vehicles from uploaded videos using computer vision techniques. It generates a vehicle distribution chart for visual analysis, aiding in traffic management and urban planning.

Vehicle tracking involves identifying and following vehicle movements through video surveillance, playing a crucial role in modern traffic monitoring systems. This application supports key functions such as traffic flow analysis, vehicle counting, and public safety—all in a cost-effective and scalable solution.

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

### 1. Landing Page

![Landing Page](Screenshots/Landing%20Page.png)

### 2. Uplaod Video Page

![Upload Video Page](Screenshots/Upload%20Video%20Page.png)

### 3. Vehicle Detection and Counting

![Vehicle Detection and Counting](Screenshots/Vehicle%20Detection%20and%20Counting.png)

### 4. Vehicle Distribution Chart

![Vehicle Distribution Chart](Screenshots/Vehicle%20Distribution%20Chart.png)
