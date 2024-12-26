# SignLanguageDetector
End-To-End Sign Language Detector. <br>
I have taken down the live project from AWS but you can still run the project locally by following the below instructions.

## Workflow

- constant
- config_entity
- artifact-entity
- components
- pipeline
- app.py

## Project Configuration 
```bash
#install aws cli from the following link

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```

```bash
#Configure aws crediential (secret key & access key)

aws configure
```


```bash
#Create a s3 bucket for model pusher. name is mentioned in the consrtant

```

## How to run
```bash
conda create -n signlang python==3.7
```
```bash
conda activate signlang
```

```bash
pip install -r requirements.txt
```

```bash
git clone https://github.com/ultralytics/yolov5.git
```
```bash
python app.py
```
