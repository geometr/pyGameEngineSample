# pylint: skip-file
# flake8: noqa
import pytest

import pygame
import screen
import local_time

def test_calculate_times_of_day():
    local_times = local_time.Time()

    assert local_times.times_of_day == "night"

def test_get_steps_in_century():
    local_times = local_time.Time()
    local_times.years_in_century = 40

    assert local_times.get_steps_in_century() == local_times.get_steps_in_year()*40

def test_tick():
    local_times = local_time.Time()
    local_times.current_hour = 0
    local_times.tick()
    assert local_times.current_hour == 1
    local_times.current_hour = 10
    local_times.hours_in_day = 11
    local_times.tick()
    assert local_times.current_hour == 0
    local_times.days_in_year = 365
    local_times.current_hour = 23
    local_times.hours_in_day = 24
    local_times.current_day = 364
    local_times.tick()
    assert local_times.current_day == 0
    local_times.current_hour = 9
    local_times.tick()
    assert local_times.times_of_day == "morning"
    local_times.tick()
    assert local_times.times_of_day == "day"
    local_times.current_hour = 15
    local_times.tick()
    assert local_times.times_of_day == "evening"
    local_times.current_hour = 21
    local_times.tick()
    assert local_times.times_of_day == "night"

def test_notify_need_to_render():
    local_times = local_time.Time()
    scr = screen.Screen()
    target_rects = []
    target_rects.append(pygame.Rect(0,0,0,0))
    target_rects.append(pygame.Rect(10,10,336,17))
    rects = []
    local_times.notify_need_to_render(scr,rects)
    assert rects == target_rects
