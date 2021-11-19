from requests import post

for i in range(10):
    result = post('http://127.0.0.1:5000/', json={"id": "None",
                                                  "type_room": 1,
                                                  "cur_count_passengers": 0,
                                                  "max_count_passenger": 2,
                                                  "tenants": [],
                                                  "is_free": True,
                                                  "address": i,
                                                  "place": 1})
    print(result)
    print(result.status_code)