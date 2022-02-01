# pylint: skip-file
# flake8: noqa
import pytest

import pygame
import screen
import temperature


def test_get_temperature():
    temp = temperature.Temperature()

    assert temp.get_temperature() > temp.global_temperature - temp.maximal_delta / 2
    assert temp.get_temperature() < temp.global_temperature + temp.maximal_delta / 2

def test_notify_hour_changed():
    temp = temperature.Temperature()
    local_temp = temp.local_temperature
    temp.notify_hour_changed("evening")
    assert local_temp-0.5 == temp.local_temperature
    temp.notify_hour_changed("morning")
    assert local_temp == temp.local_temperature
    temp.notify_hour_changed("day")
    assert local_temp + 2 == temp.local_temperature
    temp.notify_hour_changed("night")
    assert local_temp + 1 == temp.local_temperature

def test_notify_day_changed():
    temp_winter = temperature.Temperature()
    temp_winter.notify_day_changed(20,360)
    temp_summer = temperature.Temperature()
    temp_summer.notify_day_changed(200,360)
    assert temp_winter.global_temperature < temp_summer.global_temperature

def test_notify_need_to_render():
    temp = temperature.Temperature()
    scr = screen.Screen()
    temp.need_update = True
    rects = []
    target_rects = []
    temp.local_temperature = 0
    temp.notify_need_to_render(scr,rects)
    target_rects.append(pygame.Rect(0,0,0,0))
    target_rects.append(pygame.Rect(10,10,125,16))
    assert rects == target_rects

def test_notify_screen_render():
    temp = temperature.Temperature()
    scr = screen.Screen()
    old_i_text = scr.i_text
    temp.local_temperature = 0
    temp.notify_screen_render(scr)
    assert old_i_text == scr.i_text - 30
