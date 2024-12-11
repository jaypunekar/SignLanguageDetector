import os, sys
import zipfile
import yaml
import subprocess
import shutil
from signLanguage.utils.main_utils import read_yaml_file
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import ModelTrainerConfig
from signLanguage.entity.artifacts_entity import ModelTrainerArtifact

class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config


    
    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")

            zip_file = "SignLanguageDetector.v1i.yolov5pytorch.zip"

            if os.path.exists(zip_file):
                try:
                    # Unzip the file using zipfile module (works cross-platform)
                    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                        zip_ref.extractall()  # Extract all contents

                    # Remove the zip file after extraction
                    os.remove(zip_file)
                    logging.info(f"{zip_file} was successfully extracted and removed.")

                except zipfile.BadZipFile:
                    logging.info(f"Error: {zip_file} is not a valid zip file.")
            else:
                logging.info(f"{zip_file} does not exist!")

            # os.system("unzip SignLanguageDetector.v1i.yolov5pytorch.zip")
            # os.system("rm SignLanguageDetector.v1i.yolov5pytorch.zip")

            with open("data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])

            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            logging.info(model_config_file_name)

            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")

            config['nc'] = int(num_classes)


            with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)

            # Ensure paths are correct
            yolov5_path = "yolov5"
            cfg_path = "./models/custom_yolov5s.yaml"

            # Format the command with correct paths
            train_command = f"cd {yolov5_path}/ && python train.py --img 640 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg {cfg_path} --weights {self.model_trainer_config.weight_name} --name yolov5s_results --cache"

            # Now, execute the command
            os.system(train_command)


            # subprocess.run(train_command, shell=True, check=True)

            source_path = os.path.abspath("yolov5/runs/train/yolov5s_results/weights/best.pt")
            destination_path = os.path.abspath("yolov5/")

            copy_command = f'copy "{source_path}" "{destination_path}"'
            try:
                subprocess.run(copy_command, shell=True, check=True)
                print("File copied successfully!")
            except subprocess.CalledProcessError as e:
                print(f"Error occurred: {e}")

            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            source = "yolov5/runs/train/yolov5s_results/weights/best.pt"
            destination = f"{self.model_trainer_config.model_trainer_dir}/"

            # Use shutil to perform the copy operation
            shutil.copy(source, destination)

            # copy_command = f"copy yolov5/runs/train/yolov5s_results/weights/best.pt {self.model_trainer_config.model_trainer_dir}/"

            # subprocess.run(copy_command, shell=True, check=True)
           
            shutil.rmtree("yolov5/runs")
            shutil.rmtree("train")
            shutil.rmtree("test")
            shutil.rmtree("valid")
            os.remove("data.yaml")
            os.remove("README.roboflow.txt")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov5/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact


        except Exception as e:
            raise SignException(e, sys)