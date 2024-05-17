import logging
import random

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def extract_comms_action(message):
    # Extract action from results
    log.info(f"Extracting action from results: {message}")
    # setting action to be OK araound 80% of the time
    action = random.choice(['OK', 'OK', 'OK', 'OK', 'not OK'])
    return action


def take_action(action):
    log.info(f"Taking action: {action}")
