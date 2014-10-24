#encoding: utf-8

from nose.tools import *
import sys
sys.path.append('../lib')


from minutes_and_hours import minutes_to_hours_and_minutes




@raises(TypeError)
def test_fakultet_takes_a_tal_as_argument():
    minutes_to_hours_and_minutes()


def test_150_minutes_should_give2_30():

    assert_equal(minutes_to_hours_and_minutes(150), '2:30')

def test_45_minutes_should_give0_45():

    assert_equal(minutes_to_hours_and_minutes(45), '0:45')

def test_0_minutes_should_give0_0():

    assert_equal(minutes_to_hours_and_minutes(0), '0:00')

def test_64_minutes_should_give1_04():

    assert_equal(minutes_to_hours_and_minutes(64), '1:04')