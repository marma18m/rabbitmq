from pydantic import BaseModel, Field
from typing import List, Optional


class MessageJSON:
    def __init__(self):
        self.message = {
            "timestamp": None,
            "acquisitionDeviceInfo": {"id": None, "name": None},
            "imageInfo": {"id": None, "recipeID": None, "path": None},
            "inferenceServiceID": None,
            "ResultInfo": {
                "resultTimestamp": None,
                "resultPath": None,
                "commsResultPath": None,
                "imageWithGraphicsPath": None,
            },
        }

    def set_timestamp(self, timestamp):
        self.message["timestamp"] = timestamp

    def set_acquisition_device_info(self, id, name):
        self.message["acquisitionDeviceInfo"]["id"] = id
        self.message["acquisitionDeviceInfo"]["name"] = name

    def set_image_info(self, id, recipeID, path):
        self.message["imageInfo"]["id"] = id
        self.message["imageInfo"]["recipeID"] = recipeID
        self.message["imageInfo"]["path"] = path

    def set_inference_service_id(self, id):
        self.message["inferenceServiceID"] = id

    def set_result_info(
        self,
        resultTimestamp,
        resultPath,
        commsResultPath,
        imageWithGraphicsPath,
    ):
        self.message["ResultInfo"]["resultTimestamp"] = resultTimestamp
        self.message["ResultInfo"]["resultPath"] = resultPath
        self.message["ResultInfo"]["commsResultPath"] = commsResultPath
        self.message["ResultInfo"][
            "imageWithGraphicsPath"
        ] = imageWithGraphicsPath

    def get_message(self):
        return self.message


class AcquisitionDevice(BaseModel):
    id: int
    name: str


class Image(BaseModel):
    id: int
    recipeID: int
    path: str


class ResultAnalysis(BaseModel):
    resultTimestamp: int
    resultPath: str
    commsResultPath: str
    imageWithGraphicsPath: str


class Message(BaseModel):
    timestamp: int
    acquisitionDeviceInfo: AcquisitionDevice
    imageInfo: Image
    inferenceServiceID: int
    ResultInfo: ResultAnalysis


# to validate the data given a json
# try:
#     user = User(**user_json)
#     print(user.json(indent=4))
# except ValidationError as e:
#     print("Validation Error:", e.json())
