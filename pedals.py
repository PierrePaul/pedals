#!/usr/bin/python3
import evdev
from pynput.keyboard import Key, Controller
keyboard = Controller()

device_name = 'Logitech G29'
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
device = None
for device_info in devices:
    if device_name in device_info.name:
        device = device_info

 
pressing_alt = False
pressing_ctrl = False
pressing_super = False
for event in device.read_loop():
    if event.code != 0 and event.value != 0:
        #print(event)
        pass

    if event.code == 2 and event.value < 200 and pressing_alt is False:
        keyboard.press(Key.cmd_l)
        pressing_alt = True
    if event.code == 2 and event.value > 200 and pressing_alt is True:
        keyboard.release(Key.cmd_l)
        pressing_alt = False

    if event.code == 5 and event.value < 200 and pressing_super is False:
        keyboard.press(Key.alt_l)
        pressing_super = True
    if event.code == 5 and event.value > 200 and pressing_super is True:
        keyboard.release(Key.alt_l)
        pressing_super = False

    if event.code == 1 and event.value < 200 and pressing_ctrl is False:
        keyboard.press(Key.ctrl_l)
        pressing_ctrl = True
    if event.code == 1 and event.value > 200 and pressing_ctrl is True:
        keyboard.release(Key.ctrl_l)
        pressing_ctrl = False
