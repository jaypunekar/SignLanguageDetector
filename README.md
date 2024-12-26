# Sign Language Detector Web App

This project is a web application for real-time sign language detection using Flask and YOLOv5. The application leverages computer vision techniques to identify and interpret sign language gestures, providing a bridge for communication with the hearing-impaired community.
<br>
<br>
#### Note: You don't have to follow docker and AWS setup you can just run the app locally by using installing requirements.txt, YoloV5 and running app.py


## Features

- **Real-Time Detection**: Uses YOLOv5 for accurate and efficient sign language detection.
- **Web Interface**: User-friendly interface built with Flask.
- **Scalable Deployment**: Hosted on AWS for high availability and performance.
- **Containerized Application**: Dockerized for seamless deployment and portability.

## Technologies Used

- **Backend Framework**: Flask
- **Object Detection**: YOLOv5
- **Cloud Hosting**: AWS
- **Containerization**: Docker
- **Programming Language**: Python

## Installation

### Prerequisites
- Python 3.8+
- Docker
- AWS Account (if deploying on AWS)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jaypunekar/SignLanguageDetector.git
   cd SignLanguageDetector
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download YOLOv5 Model**:
   - Follow the instructions on the [YOLOv5 repository](https://github.com/ultralytics/yolov5) to download the pre-trained weights.
   - Place the weights in the `models/` directory.

4. **Run the Application**:
   ```bash
   python app.py
   ```
   - Access the web application at `http://localhost:5000`.

### Docker Deployment

1. **Build the Docker Image**:
   ```bash
   docker build -t SignLanguageDetector .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 SignLanguageDetector
   ```

3. **Access the Application**:
   - Open your browser and go to `http://localhost:5000`.

### AWS Deployment

1. **Push Docker Image to AWS ECR**:
   - Follow the [AWS ECR documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) to create a repository and push your Docker image.

2. **Deploy Using AWS ECS or EC2**:
   - Use ECS or EC2 to run the Docker container.
   - Ensure the necessary ports are open for external access.

## Usage

1. Open the web application in your browser.
2. Upload a video or use your webcam for real-time detection.
3. View the results, including detected gestures and their corresponding meanings.

## Project Structure

```
.
├── data/
│   └── .gitkeep
├── {project_name}/
│   ├── __init__.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── model_trainer.py
│   │   └── model_pusher.py
│   ├── configuration/
│   │   ├── __init__.py
│   │   └── s3_operations.py
│   ├── constant/
│   │   ├── __init__.py
│   │   ├── training_pipeline/
│   │   │   └── __init__.py
│   │   └── application.py
│   ├── entity/
│   │   ├── __init__.py
│   │   ├── artifacts_entity.py
│   │   └── config_entity.py
│   ├── exception/
│   │   └── __init__.py
│   ├── logger/
│   │   └── __init__.py
│   ├── pipeline/
│   │   ├── __init__.py
│   │   └── training_pipeline.py
│   └── utils/
│       ├── __init__.py
│       └── main_utils.py
├── templates/
│   └── index.html
├── .dockerignore
├── app.py
├── Dockerfile
├── requirements.txt
├── setup.py
└── README.md
```


## Acknowledgments

- [YOLOv5](https://github.com/ultralytics/yolov5) for the object detection model.
- Flask is for lightweight and flexible web frameworks.
- AWS for cloud hosting services.

---

Feel free to update the repository link, acknowledgements, or any other sections as needed.


```bash
git clone https://github.com/ultralytics/yolov5.git
```
```bash
python app.py
```
