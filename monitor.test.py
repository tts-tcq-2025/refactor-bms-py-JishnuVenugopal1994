import unittest
from unittest.mock import patch
from monitor import VitalSignsMonitor

class TestVitalSignsMonitor(unittest.TestCase):
  def setUp(self):
    # Create a new instance of VitalSignsMonitor before each test
    self.monitor = VitalSignsMonitor()

  @patch('monitor.VitalSignsMonitor.print_visual_effect')
  def test_temperature_monitoring_normal(self, mock_alert):
    # Test normal temperature value; should return True and not alert
    self.assertTrue(self.monitor.temperature_monitoring(98.6))
    mock_alert.assert_not_called()

  @patch('monitor.VitalSignsMonitor.print_visual_effect')
  def test_temperature_monitoring_low(self, mock_alert):
    # Test low temperature; should return False and alert
    self.assertFalse(self.monitor.temperature_monitoring(94))
    mock_alert.assert_called_once_with('Temperature critical!')

  @patch('monitor.VitalSignsMonitor.print_visual_effect')
  def test_temperature_monitoring_high(self, mock_alert):
    # Test high temperature; should return False and alert
    self.assertFalse(self.monitor.temperature_monitoring(103))
    mock_alert.assert_called_once_with('Temperature critical!')

  @patch('monitor.VitalSignsMonitor.print_visual_effect')
  def test_pulse_rate_monitoring_normal(self, mock_alert):
    # Test normal pulse rate; should return True and not alert
    self.assertTrue(self.monitor.pulse_rate_monitoring(75))
    mock_alert.assert_not_called()

  @patch('monitor.VitalSignsMonitor.print_visual_effect')
  def test_pulse_rate_monitoring_low(self, mock_alert):
    # Test low pulse rate; should return False and alert
    self.assertFalse(self.monitor.pulse_rate_monitoring(50))
    mock_alert.assert_called_once_with('Pulse Rate critical!')

  @patch('monitor.VitalSignsMonitor.print_visual_effect')
  def test_pulse_rate_monitoring_high(self, mock_alert):
    # Test high pulse rate; should return False and alert
    self.assertFalse(self.monitor.pulse_rate_monitoring(120))
    mock_alert.assert_called_once_with('Pulse Rate critical!')

  @patch('monitor.VitalSignsMonitor.print_visual_effect')
  def test_spo2_monitoring_normal(self, mock_alert):
    # Test normal SpO2 value; should return True and not alert
    self.assertTrue(self.monitor.spo2_monitoring(95))
    mock_alert.assert_not_called()

  @patch('monitor.VitalSignsMonitor.print_visual_effect')
  def test_spo2_monitoring_low(self, mock_alert):
    # Test low SpO2 value; should return False and alert
    self.assertFalse(self.monitor.spo2_monitoring(85))
    mock_alert.assert_called_once_with('Oxygen Saturation critical!')

  @patch('monitor.VitalSignsMonitor.print_visual_effect')
  def test_temperature_monitoring_custom_thresholds(self, mock_alert):
    # Test temperature with custom thresholds: low=90, high=100
    # Value is above high threshold; should return False and alert
    self.assertFalse(self.monitor.temperature_monitoring(101, 90, 100))
    mock_alert.assert_called_once_with('Temperature critical!')

  @patch('monitor.VitalSignsMonitor.print_visual_effect')
  def test_pulse_rate_monitoring_custom_thresholds(self, mock_alert):
    # Test pulse rate with custom thresholds: low=70, high=80
    # Value is below low threshold; should return False and alert
    self.assertFalse(self.monitor.pulse_rate_monitoring(65, 70, 80))
    mock_alert.assert_called_once_with('Pulse Rate critical!')

  @patch('monitor.VitalSignsMonitor.print_visual_effect')
  def test_spo2_monitoring_custom_threshold(self, mock_alert):
    # Test SpO2 with custom threshold: 95
    # Value is below threshold; should return False and alert
    self.assertFalse(self.monitor.spo2_monitoring(90, 95))
    mock_alert.assert_called_once_with('Oxygen Saturation critical!')

if __name__ == '__main__':
  unittest.main()
