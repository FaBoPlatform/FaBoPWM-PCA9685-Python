# coding: utf-8
import unittest
import Fabo_PCA9685
import time

import pkg_resources
SMBUS='smbus'
for dist in pkg_resources.working_set:
    #print(dist.project_name, dist.version)
    if dist.project_name == 'smbus':
        break
    if dist.project_name == 'smbus2':
        SMBUS='smbus2'
        break
if SMBUS == 'smbus':
    import smbus
elif SMBUS == 'smbus2':
    import smbus2 as smbus
    #import Adafruit_PureIO.smbus as smbus


class TestPCA9685(unittest.TestCase):

    def setUp(self):
        '''
        smbus準備
        '''
        busnum = 1 # bus番号
        self.bus = smbus.SMBus(busnum)
        self.assertNotEqual(self.bus, None)
        '''
        PCA9685準備
        '''
        self.PCA9685 = Fabo_PCA9685.PCA9685(self.bus)
        self.assertNotEqual(self.PCA9685, None)

        '''
        PCA9685 Hz設定
        '''
        hz = 60
        prescale = self.PCA9685.calc_prescale(hz)
        self.PCA9685.set_prescale(prescale)
        value = self.PCA9685.get_prescale()
        self.assertEqual(prescale, value)
        
        return

    @unittest.skip("skipping")
    def test_set_prescale(self):
        hz = 60
        prescale = self.PCA9685.calc_prescale(hz)
        self.PCA9685.set_prescale(prescale)
        value = self.PCA9685.get_prescale()
        self.assertEqual(prescale, value)
        return

    def test_set_freq(self):
        hz = 61
        prescale = self.PCA9685.calc_prescale(hz)
        self.PCA9685.set_freq(hz)
        value = self.PCA9685.get_prescale()
        self.assertEqual(prescale, value)
        return

    @unittest.skip("skipping")
    def test_set_prescale_loop(self):
        min_hz = 24
        max_hz = 1000
        for hz in range(min_hz,max_hz+1):
            prescale = self.PCA9685.calc_prescale(hz)
            self.PCA9685.set_prescale(prescale)
            value = self.PCA9685.get_prescale()
            self.assertEqual(prescale, value)
        return

    def test_channel_value_min(self):
        min_value = 150
        channel = 2
        self.PCA9685.set_channel_value(channel,min_value)
        value = self.PCA9685.get_channel_value(channel)
        self.assertEqual(min_value, value)
        time.sleep(1)

    def test_channel_value_cen(self):
        cen_value = 300
        channel = 2
        self.PCA9685.set_channel_value(channel,cen_value)
        value = self.PCA9685.get_channel_value(channel)
        self.assertEqual(cen_value, value)
        time.sleep(1)

    def test_channel_value_max(self):
        max_value = 600
        channel = 2
        self.PCA9685.set_channel_value(channel,max_value)
        value = self.PCA9685.get_channel_value(channel)
        self.assertEqual(max_value, value)
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
    
    
