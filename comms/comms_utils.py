import logging
import random

log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)


def extract_results_action(message):
    # Extract action from results
    log.warning(f"Extracting action from results: {message}")
    # setting action to be OK araound 80% of the time
    action = random.choice(['OK', 'OK', 'OK', 'OK', 'not OK'])
    return action


def take_action(action):
    log.warning(f"Taking action: {action}")
