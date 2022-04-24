#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid
from datetime import datetime


class Segway:

    def __init__(
        self,
        id_segway,
        model,
        velocity,
        battery,
        state,
        mileage=0,
        created=None,
        ):
        self.id_segway  = id_segway
        self.model      = model
        self.velocity   = velocity
        self.battery    = battery
        self.state      = state
        self.created    = created or datetime.now()
        self.mileage    = mileage or 0
        self.rent_start = None
        self.used       = True

    def start_rent(self):
        self.rent_start = datetime.now()
        self.used = True

    def stop_rent(self):
        self.battery -= (datetime.now() - self.rent_start).total_seconds()
        self.state -= (datetime.now() - self.rent_start).total_seconds() / 2
        self.mileage += (datetime.now() - self.rent_start).total_seconds() / 2
        self.rent_start = None

    def has_ever_been_rented(self):
        return self.used


class SegwayDepot:

    def __init__(self):
        self.segways = []

    def get_availible(self):
        result = []
        if len(self.segways) == 0:
            return result

        for segway in self.segways:
            if segway.rent_start is None:
                result.append(segway)

        return result

    def add(self, segway):
        already_in_depot = False
        for existing_segway in self.segways:
            if existing_segway.id_segway == segway.id_segway:
                already_in_depot = True

        if already_in_depot == False:
            self.segways.append(segway)

    def get_number_of_segways(self):
        return len(self.segways)

    def rent(self, id_segway):
        selected_segway = None
        for segway in self.segways:
            if segway.id_segway == id_segway:
                selected_segway = segway
                break
        
        if selected_segway is None:
            return False
        
        if selected_segway.rent_start is not None:
            return False

        if selected_segway.battery < 25 or selected_segway.state < 50:
            return False

        selected_segway.start_rent()
        return True
        

    def rent_stop(self, id_segway):

        selected_segway = None
        for segway in self.segways:
            if segway.id_segway == id_segway:
                selected_segway = segway
                break
                
        if selected_segway is None:
            return False
            
        if selected_segway.rent_start is None:
            return False

        selected_segway.stop_rent()
        return True


def main():
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

    depot.add(segway1)
    depot.add(segway2)
    depot.add(segway3)

    print('Now' + str(depot.get_number_of_segways()) + ' segways.')
    
    print('Available segways:')
    for segway in depot.get_availible():
        print('id ' + str(segway.id_segway) + ' model ' + str(segway.model) + ' battery ' + str(segway.battery))

    depot.rent(2)
    
    print('Available segways:')
    for segway in depot.get_availible():
        print('id ' + str(segway.id_segway) + ' model '+ str(segway.model) + ' battery ' + str(segway.battery))

    print(depot.rent(2))
    
    depot.rent_stop(2)
    
    print('Available segways:')
    for segway in depot.get_availible():
        print('id ' + str(segway.id_segway) + ' model '+ str(segway.model) + ' battery ' + str(segway.battery))


main()

# empty depot + 1 samokat = 

