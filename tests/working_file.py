import json
from pydantic import BaseModel

class SensorReading(BaseModel):
    sensor_id: str
    value: float
    

dic = {
    "sensor_id": "sensor0123",
    "value": 35
}

sensor_reading = SensorReading(**dic)
print(sensor_reading)
print(type(sensor_reading))

as_dict = sensor_reading.model_dump()
print(as_dict)
print(type(as_dict))

as_json = sensor_reading.model_dump_json()
print(as_json)
print(type(as_json))

'''
print(type(dic))
print(dic["thomas"])

print(dic.get("eten"))

print(dic)
jsonversie = json.dumps(dic)
print(type(jsonversie))

'''
