add_library('minim')

import events as Events
import os
import copy
import util

window_width = 800
window_height = 800

def setup():
    size(window_width, window_height, P3D)

    try:
        import arcade_gui as ARC
        import events as EVENTS

        global arcade_state
        global keyboard
        global mouse
        
        keyboard = EVENTS.KeyBoard_Event()
        mouse = EVENTS.Mouse_Event()
        
        arcade_state = ARC.Arcade(Minim(this), keyboard, mouse)
        arcade_state.resize(window_width, window_height)
    except Exception as ex:
        util.Error.log("Initialization", ex)

def draw():
    try:
        global window_width
        global window_height
        global arcade_state

        if window_width != width or window_height != height:
            window_width = width
            window_height = height
            arcade_state.resize(window_width, window_height)

        arcade_state.update()
    except Exception as ex:
        util.Error.log("Rendering", ex)


def keyPressed():
    try:
        keyboard.press()
        try:
            if this.key == ESC:
                this.key = " "
        except:
            pass
    except Exception as ex:
        util.Error.log("Input", "Key Pressed", ex)

def keyReleased():
    try:
        keyboard.release()
    except Exception as ex:
        util.Error.log("Input", "Key Released", ex)

def mousePressed():
    try:
        mouse.press()
    except Exception as ex:
        util.Error.log("Input", "Mouse Pressed", ex)

def mouseReleased():
    try:
        mouse.release()
    except Exception as ex:
        util.Error.log("Input", "Mouse Pressed", ex)

def mouseMoved():
    try:
        mouse.release()
        mouse.move()
    except Exception as ex:
        util.Error.log("Input", "Mouse Moved", ex)

def mouseDragged():
    try:
        mouse.press()
        mouse.move()
    except Exception as ex:
        util.Error.log("Input", "Mouse Dragged", ex)
