import logging
import random
import time
from schemas.comms_message import CommsMessageJSON

log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)


def predict_result(image_path):
    # genereate random result [OK, not OK]
    result = random.choice(['OK', 'not OK'])
    timestamp = int(time.time())
    log.warning(f'Predicted result for image {image_path} is {result}')

    return result, timestamp


def parse_result_to_comms_message(result, comms_message: CommsMessageJSON):
    # tag one of Trigger, LoadRecipe, RecipeID, Ok, NotOk
    tags = ['Trigger', 'LoadRecipe', 'RecipeID', 'Ok', 'NotOk']
    tag = random.choice(tags)
    value = random.randint(0, 1)
    comms_message.set_tag(tag)
    comms_message.set_value(value)

    return comms_message
