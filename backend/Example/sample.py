from example import reset_all
from example import create_room

from requests import post

json_data = {"id": "None",
             "place_in_address": 1,
             "place_in_room": 1,
             "gender": True,
             "age": 30,
             "desire_communicate": False,
             "vaccination_against_covid19": False,
             "hasPet": False,
             "hasChild": False,
             "smoking": False,
             "interests": [2, 3],
             "date_start": 1637414754840,
             "date_end": 1637414754840,
             "neighborsAge": [25, 50],
             "neighborsHasPet": False,
             "neighborsSmoking": False,
             "neighborsHasChild": True,
             }
result = post('http://127.0.0.1:5000/add/tenant', json=json_data)
print(result)
print(result.status_code)

json_data = {"id": "None",
             "place_in_address": 1,
             "place_in_room": 2,
             "gender": True,
             "age": 28,
             "desire_communicate": False,
             "vaccination_against_covid19": False,
             "hasPet": False,
             "hasChild": False,
             "smoking": False,
             "interests": [2],
             "date_start": 1637414754840,
             "date_end": 1637414754840,
             "neighborsAge": [20, 40],
             "neighborsHasPet": False,
             "neighborsSmoking": False,
             "neighborsHasChild": True,
             }
result = post('http://127.0.0.1:5000/add/tenant', json=json_data)
print(result)
print(result.status_code)

json_data = {"id": "None",
             "place_in_address": 2,
             "place_in_room": 1,
             "gender": True,
             "age": 18,
             "desire_communicate": True,
             "vaccination_against_covid19": False,
             "hasPet": False,
             "hasChild": False,
             "smoking": False,
             "interests": [1],
             "date_start": 1637414754840,
             "date_end": 1637414754840,
             "neighborsAge": [1, 25],
             "neighborsHasPet": True,
             "neighborsSmoking": True,
             "neighborsHasChild": True,
             }
result = post('http://127.0.0.1:5000/add/tenant', json=json_data)
print(result)
print(result.status_code)

json_data = {"id": "None",
             "place_in_address": 3,
             "place_in_room": 4,
             "gender": True,
             "age": 50,
             "desire_communicate": True,
             "vaccination_against_covid19": True,
             "hasPet": False,
             "hasChild": False,
             "smoking": False,
             "interests": [1, 2, 3],
             "date_start": 1637414754840,
             "date_end": 1637414754840,
             "neighborsAge": [1, 70],
             "neighborsHasPet": False,
             "neighborsSmoking": False,
             "neighborsHasChild": True,
             }
result = post('http://127.0.0.1:5000/add/tenant', json=json_data)
print(result)
print(result.status_code)

json_data = {"id": "None",
             "place_in_address": 3,
             "place_in_room": 1,
             "gender": False,
             "age": 30,
             "desire_communicate": True,
             "vaccination_against_covid19": True,
             "hasPet": False,
             "hasChild": False,
             "smoking": False,
             "interests": [1, 2, 3],
             "date_start": 1637414754840,
             "date_end": 1637414754840,
             "neighborsAge": [1, 70],
             "neighborsHasPet": False,
             "neighborsSmoking": False,
             "neighborsHasChild": True,
             }
result = post('http://127.0.0.1:5000/add/tenant', json=json_data)
print(result)
print(result.status_code)

json_data = {"id": "None",
             "place_in_address": 4,
             "place_in_room": 2,
             "gender": False,
             "age": 20,
             "desire_communicate": True,
             "vaccination_against_covid19": False,
             "hasPet": False,
             "hasChild": False,
             "smoking": False,
             "interests": [4],
             "date_start": 1637414754840,
             "date_end": 1637414754840,
             "neighborsAge": [20, 30],
             "neighborsHasPet": False,
             "neighborsSmoking": False,
             "neighborsHasChild": True,
             }
result = post('http://127.0.0.1:5000/add/tenant', json=json_data)
print(result)
print(result.status_code)

json_data = {"id": "None",
             "place_in_address": 4,
             "place_in_room": 3,
             "gender": False,
             "age": 20,
             "desire_communicate": True,
             "vaccination_against_covid19": False,
             "hasPet": False,
             "hasChild": False,
             "smoking": False,
             "interests": [4],
             "date_start": 1637414754840,
             "date_end": 1637414754840,
             "neighborsAge": [20, 30],
             "neighborsHasPet": False,
             "neighborsSmoking": False,
             "neighborsHasChild": True,
             }
result = post('http://127.0.0.1:5000/add/tenant', json=json_data)
print(result)
print(result.status_code)

json_data = {"id": "None",
             "place_in_address": 5,
             "place_in_room": 3,
             "gender": True,
             "age": 23,
             "desire_communicate": True,
             "vaccination_against_covid19": False,
             "hasPet": False,
             "hasChild": False,
             "smoking": False,
             "interests": [4],
             "date_start": 1637414754840,
             "date_end": 1637414754840,
             "neighborsAge": [20, 30],
             "neighborsHasPet": False,
             "neighborsSmoking": True,
             "neighborsHasChild": True,
             }
result = post('http://127.0.0.1:5000/add/tenant', json=json_data)
print(result)
print(result.status_code)

json_data = {"id": "None",
             "place_in_address": 5,
             "place_in_room": 4,
             "gender": False,
             "age": 21,
             "desire_communicate": True,
             "vaccination_against_covid19": False,
             "hasPet": False,
             "hasChild": False,
             "smoking": False,
             "interests": [4],
             "date_start": 1637414754840,
             "date_end": 1637414754840,
             "neighborsAge": [20, 30],
             "neighborsHasPet": False,
             "neighborsSmoking": True,
             "neighborsHasChild": True,
             }
result = post('http://127.0.0.1:5000/add/tenant', json=json_data)
print(result)
print(result.status_code)

json_data = {"id": "None",
             "place_in_address": 6,
             "place_in_room": 2,
             "gender": True,
             "age": 30,
             "desire_communicate": True,
             "vaccination_against_covid19": False,
             "hasPet": False,
             "hasChild": False,
             "smoking": False,
             "interests": [2, 3],
             "date_start": 1637414754840,
             "date_end": 1637414754840,
             "neighborsAge": [25, 50],
             "neighborsHasPet": False,
             "neighborsSmoking": False,
             "neighborsHasChild": True,
             }
result = post('http://127.0.0.1:5000/add/tenant', json=json_data)
print(result)
print(result.status_code)

json_data = {"id": "None",
             "place_in_address": 6,
             "place_in_room": 4,
             "gender": True,
             "age": 28,
             "desire_communicate": True,
             "vaccination_against_covid19": False,
             "hasPet": False,
             "hasChild": False,
             "smoking": False,
             "interests": [2],
             "date_start": 1637414754840,
             "date_end": 1637414754840,
             "neighborsAge": [20, 40],
             "neighborsHasPet": False,
             "neighborsSmoking": False,
             "neighborsHasChild": True,
             }
result = post('http://127.0.0.1:5000/add/tenant', json=json_data)
print(result)
print(result.status_code)