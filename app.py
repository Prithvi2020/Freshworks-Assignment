import json
import time
import threading
from threading import*
import sys

datastore={}

def create(key,value,Time_to_live=0):
    if(key in datastore):
        print("Cannot create key-value pair for this given key since the given key already exists in the datastore.")
    else:
        if(key.isalpha()):
            if(len(datastore)<(1024*1024*1024) and sys.getsizeof(value)<=(16*1024)):
                if(Time_to_live==0):
                    temp=[value,Time_to_live]
                else:
                    temp=[value,time.time()+Time_to_live]
                if(len(key)<=32):
                    datastore[key]=temp
                    d=datastore[key]
                    print("The Key = {0} : Value = {1} is inserted successfully.".format(key,d[0]))
                else:
                    print("The key exceeded 32 characters")
            else:
                print("The memory constraints does not match. The size of the datastore should be less than 1GB and the size of the JsonObject value should be less than 16KB.")
                
        else:
            print("The name of the entered key is Invalid. The name of the key should be a string with no numbers or special characters.")


def read(key):
    if(key not in datastore):
        print("The given key does not exists in the datastore. Kindly enter a valid key.")
    
    else:
        d=datastore[key]
        if(d[1]!=0):
            if(time.time()<=d[1]):
                print("Key = {0} : Value = {1}".format(key,str(d[0])))
            else:
                print("The Time-to-Live of {0} has expired.".format(key))
        else:
            print("Key = {0} : Value = {1}".format(key,str(d[0])))


def delete(key):
    if(key not in datastore):
        print("The given key does not exists in the datastore. Kindly enter a valid key.")
    else:
        d=datastore[key]
        if(d[1]!=0):
            if(time.time()<=d[1]):
                del datastore[key]
                print("The Key : {0} is successfully deleted.".format(key))
            else:
                print("The Time-to-Live of {0} has expired.".format(key))
        else:
            del datastore[key]
            print("The Key : {0} is successfully deleted.".format(key))


def save():
    d=datastore
    with open('save.json','w') as file:
        json.dump(d,file)
        
    
