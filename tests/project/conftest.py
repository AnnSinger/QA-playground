import pytest
from src.project import Segway
from src.project import SegwayDepot

@pytest.fixture()
def empty_depot():
    """Returns SegwayDepot instance with place 0"""
    return SegwayDepot()

@pytest.fixture(scope='class')
def full_depot(request):
    """Returns SegwayDepot instance with 5 segways"""
    depot = SegwayDepot()

    segway1 = Segway(
        id_segway=1,
        model='Urent',
        velocity=30,
        battery=68,
        state=78,
        mileage=256,
    )

    segway2 = Segway(
        id_segway=2,
        model='Urent',
        velocity=30,
        battery=98,
        state=60,
        mileage=120,
    )

    segway3 = Segway(
        id_segway=3,
        model='Yandex',
        velocity=20,
        battery=89,
        state=99
    )
    segway4 = Segway(
        id_segway=3,
        model='Yandex',
        velocity=20,
        battery=15,
        state=99
    )
    segway5 = Segway(
        id_segway=3,
        model='Yandex',
        velocity=20,
        battery=26,
        state=30
    )

    depot.add(segway1)
    depot.add(segway2)
    depot.add(segway3)
    depot.add(segway4)
    depot.add(segway5)

    def finalize_depot():
        depot.segways = []

    request.addfinalizer(finalize_depot)

    return depot

