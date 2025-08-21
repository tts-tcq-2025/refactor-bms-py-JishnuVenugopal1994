
from time import sleep
import sys


# Global thresholds
TEMPERATURE_THRESHOLDS = [95, 102]  # Fahrenheit [low, high]
PULSE_RATE_THRESHOLDS = [60, 100]   # Beats per minute [low, high]
SPO2_THRESHOLD = 90                 # Minimum acceptable SpO2

LOW_THRESHOLD = 0 # Index for low threshold
HIGH_THRESHOLD = 1 # Index for high threshold


class VitalSignsMonitor:
  def __init__(self):
    pass

  def temperature_monitoring(self, temperature, temperature_low_threshold = TEMPERATURE_THRESHOLDS[LOW_THRESHOLD],
                             temperature_high_threshold = TEMPERATURE_THRESHOLDS[HIGH_THRESHOLD]):
    """
    Check if the temperature is outside the defined thresholds.
    Print a visual alert if temperature is critical.
    Return True if temperature is within the safe range, else False.
    """
    if temperature < temperature_low_threshold or temperature > temperature_high_threshold:
      self.print_visual_effect('Temperature critical!')
      return False
    return True

  def pulse_rate_monitoring(self, pulse_rate, pulse_rate_low_threshold = PULSE_RATE_THRESHOLDS[LOW_THRESHOLD],
                             pulse_rate_high_threshold = PULSE_RATE_THRESHOLDS[HIGH_THRESHOLD]):
    """
    Monitor the pulse rate and check if it is within the safe thresholds.
    Print a visual alert if pulse rate is critical.
    Return True if pulse rate is within the safe range, else False.
    """
    if pulse_rate < pulse_rate_low_threshold or pulse_rate > pulse_rate_high_threshold:
      self.print_visual_effect('Pulse Rate critical!')
      return False
    return True

  def spo2_monitoring(self, spo2, spo2_threshold = SPO2_THRESHOLD):
    """
    Monitor the SpO2 level and check if it is above the threshold.
    Print a visual alert if SpO2 is critical.
    Return True if SpO2 is within the safe range, else False.
    """
    if spo2 < spo2_threshold:
      self.print_visual_effect('Oxygen Saturation critical!')
      return False
    return True

  def print_visual_effect(self, vital_status):
    """
    Print a visual effect to alert the user about a critical vital sign.
    Alternates printing '*' and ' *' for 6 cycles with a 1-second delay.
    """
    print(vital_status)
    for i in range(6):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(1)