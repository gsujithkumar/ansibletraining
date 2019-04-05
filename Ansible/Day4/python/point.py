#!/usr/bin/python

class Point:

   def __init__(self):
       self.x =0;
       self.y=0

   
   def setValus(self, value1, value2):
       self.x=value1;
       self.y=value2;
    
   def getX(self):
       return self.x;
    
   def getY(self):
       return self.y;

   def getSum(self):
       return self.x+self.y;

   def printValues(self):
       print('######################################');
       print('X = ', self.getX());
       print('Y = ', self.getY());
       print('Sum of X and Y = ', self.getSum());
       print('######################################');


obj1=Point();
obj1.setValus(10,20);
obj1.printValues();

obj2=Point();
obj2.setValus(100,200);
obj2.printValues();

