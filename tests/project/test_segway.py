import pytest
from src.project import Segway
from src.project import SegwayDepot

def test_empty_depot(empty_depot):
    assert empty_depot.segways == []
    assert empty_depot.get_number_of_segways() == 0

def test_add_segway(full_depot):
    assert full_depot.get_number_of_segways() == 3

def test_rent_first_segway(full_depot):
    assert full_depot.rent(1) == True

def test_rent_unavailableID_segway(full_depot):
    assert full_depot.rent(6) == False

def test_rent_unavailableBattery_segway(full_depot):
    assert full_depot.rent(4) == False
    print('\nInsufficient charge')

def test_rent_unavailableStage_segway(full_depot):
    assert full_depot.rent(5) == False
    print('\nInsufficient state')

def test_already_rent_segway(full_depot):
    assert full_depot.rent(1) # == True
    assert not full_depot.rent(1) # == False






