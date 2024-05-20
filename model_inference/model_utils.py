import logging
import random
import time

log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)


def predict_result(image_path):
    # genereate random result [OK, not OK]
    result = random.choice(['OK', 'not OK'])
    timestamp = int(time.time())
    log.warning(f'Predicted result for image {image_path} is {result}')

    return result, timestamp
