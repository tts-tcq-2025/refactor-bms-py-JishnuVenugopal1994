import unittest
from unittest.mock import patch
import monitor

# Test class for the vital_ok function in monitor module
class TestMonitorVitalOk(unittest.TestCase):
  # Test when all vitals are in the normal range; no alert should be triggered
  @patch('monitor.print_visual_effect')
  def test_all_vitals_normal(self, mock_print):
    monitor.vital_ok(98, 80, 95)
    mock_print.assert_not_called()

  # Test when temperature is critically high; should trigger temperature alert
  @patch('monitor.print_visual_effect')
  def test_temperature_critical_high(self, mock_print):
    monitor.vital_ok(103, 80, 95)
    mock_print.assert_any_call('Temperature critical!')

  # Test when temperature is critically low; should trigger temperature alert
  @patch('monitor.print_visual_effect')
  def test_temperature_critical_low(self, mock_print):
    monitor.vital_ok(94, 80, 95)
    mock_print.assert_any_call('Temperature critical!')

  # Test when pulse rate is critically high; should trigger pulse rate alert
  @patch('monitor.print_visual_effect')
  def test_pulse_rate_critical_high(self, mock_print):
    monitor.vital_ok(98, 103, 95)
    mock_print.assert_any_call('Pulse Rate is out of range!')

  # Test when pulse rate is critically low; should trigger pulse rate alert
  @patch('monitor.print_visual_effect')
  def test_pulse_rate_critical_low(self, mock_print):
    monitor.vital_ok(98, 59, 95)
    mock_print.assert_any_call('Pulse Rate is out of range!')

  # Test when SpO2 is critically low; should trigger SpO2 alert
  @patch('monitor.print_visual_effect')
  def test_spo2_critical_low(self, mock_print):
    monitor.vital_ok(98, 80, 89)
    mock_print.assert_any_call('Oxygen Saturation out of range!')

  # Test when multiple vitals are critical; all relevant alerts should be triggered
  @patch('monitor.print_visual_effect')
  def test_multiple_critical(self, mock_print):
    monitor.vital_ok(103, 103, 89)
    # All three alerts should be triggered
    self.assertIn(('Temperature critical!',), mock_print.call_args_list[0])
    self.assertIn(('Pulse Rate is out of range!',), [call.args for call in mock_print.call_args_list])
    self.assertIn(('Oxygen Saturation out of range!',), [call.args for call in mock_print.call_args_list])

# Run the tests if this file is executed directly
if __name__ == '__main__':
  unittest.main()
