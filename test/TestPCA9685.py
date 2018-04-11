# coding: utf-8
# python TestPCA9685.py
import unittest
import Fabo_PCA9685
import time

import pkg_resources
SMBUS='smbus'
for dist in pkg_resources.working_set:
    if dist.project_name == 'smbus':
        break
    if dist.project_name == 'smbus2':
        SMBUS='smbus2'
        break
if SMBUS == 'smbus':
    import smbus
elif SMBUS == 'smbus2':
    import smbus2 as smbus


class TestPCA9685(unittest.TestCase):

    def setUp(self):
        '''
        smbus準備
        '''
        busnum = 1 # bus番号
        init_value = 300 # 初期サーボ位置
        self.bus = smbus.SMBus(busnum)
        self.assertNotEqual(self.bus, None)
        '''
        PCA9685準備
        '''
        self.PCA9685 = Fabo_PCA9685.PCA9685(self.bus,value=init_value)
        self.assertNotEqual(self.PCA9685, None)

        '''
        PCA9685 Hz設定
        '''
        hz = 50
        self.PCA9685.set_hz(hz)
        value = self.PCA9685.get_hz()
        self.assertEqual(hz, value)

        return

    @unittest.skip("skipping")
    def test_set_hz(self):
        hz = 61
        self.PCA9685.set_hz(hz)
        value = self.PCA9685.get_hz()
        self.assertEqual(hz, value)
        return

    @unittest.skip("skipping")
    def test_set_hz_loop(self):
        min_hz = 24
        max_hz = 1526
        for hz in range(min_hz,max_hz+1):
            self.PCA9685.set_hz(hz)
            value = self.PCA9685.get_hz()
            self.assertEqual(hz, value)
        return

    @unittest.skip("skipping")
    def test_get_mode1(self):
        mode1 = 1 # ALLCALL(0x01=1) | RESTART(0x80=128) Hz設定
        value = self.PCA9685.get_mode1()
        self.assertEqual(mode1, value)

    @unittest.skip("skipping")
    def test_channel_value_min(self):
        min_value = 150
        channel = 0 # PWM0番目のピンのサーボ
        self.PCA9685.set_channel_value(channel,min_value)
        value = self.PCA9685.get_channel_value(channel)
        self.assertEqual(min_value, value)
        time.sleep(1)

    @unittest.skip("skipping")
    def test_channel_value_cen(self):
        cen_value = 300
        channel = 0 # PWM0番目のピンのサーボ
        self.PCA9685.set_channel_value(channel,cen_value)
        value = self.PCA9685.get_channel_value(channel)
        self.assertEqual(cen_value, value)
        time.sleep(1)

    @unittest.skip("skipping")
    def test_channel_value_max(self):
        max_value = 600
        channel = 0 # PWM0番目のピンのサーボ
        self.PCA9685.set_channel_value(channel,max_value)
        value = self.PCA9685.get_channel_value(channel)
        self.assertEqual(max_value, value)
        time.sleep(1)

    def test_correct_channel(self):
        min_value = 150
        max_value = 600

        for channel in range(0,16):
            '''
            全てのchannelをmin_valueに設定する
            '''
            self.PCA9685.set_channel_value(channel,min_value)
            value = self.PCA9685.get_channel_value(channel)
            self.assertEqual(min_value, value)

        time.sleep(1)
        for channel in range(0,16):
            '''
            全てのchannelの値を記録する
            一つずつchannelをmax_valueに設定する
            変更したchannelのvalueだけが変わっていることを確認する
            '''
            correct_values = []
            for channel in range(0,16):
                correct_values += [self.PCA9685.get_channel_value(channel)]

            for write_channel in range(0,16):
                self.PCA9685.set_channel_value(write_channel,max_value)
                write_value = self.PCA9685.get_channel_value(write_channel)
                correct_values[write_channel] = write_value
                for read_channel in range(0,16):
                    read_value = self.PCA9685.get_channel_value(read_channel)
                    self.assertEqual(correct_values[read_channel], read_value)
        time.sleep(1)
        for channel in range(0,16):
            '''
            全てのchannelの値を記録する
            一つずつchannelをmin_valueに設定する
            変更したchannelのvalueだけが変わっていることを確認する
            '''
            correct_values = []
            for channel in range(0,16):
                correct_values += [self.PCA9685.get_channel_value(channel)]

            for write_channel in range(0,16):
                self.PCA9685.set_channel_value(write_channel,min_value)
                write_value = self.PCA9685.get_channel_value(write_channel)
                correct_values[write_channel] = write_value
                for read_channel in range(0,16):
                    read_value = self.PCA9685.get_channel_value(read_channel)
                    self.assertEqual(correct_values[read_channel], read_value)
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
    
    
