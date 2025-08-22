
from time import sleep
import sys


def print_visual_effect(message):
    print(message)
    for i in range(6):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(1)

def vital_range_check(vital_value, low_threshold, high_threshold, message):
  if vital_value < low_threshold or vital_value > high_threshold:
    print_visual_effect(message)
    return False
  return True

def vital_low_threshold_check(vital_value, low_threshold, message):
  if vital_value < low_threshold:
    print_visual_effect(message)
    return False
  return True

def vital_ok(temperature, pulseRate, spo2):
  vital_range_check(temperature, 95, 102, 'Temperature critical!')
  vital_range_check(pulseRate, 60, 100, 'Pulse Rate is out of range!')
  vital_low_threshold_check(spo2, 90, 'Oxygen Saturation out of range!')