from requests import post

for i in range(1, 21):
    result = post('http://127.0.0.1:5000/add/room', json={"id": "None",
                                                          "type_room": 1,
                                                          "cur_count_tenants": 0,
                                                          "max_count_tenants": 4,
                                                          "tenants": [],
                                                          "is_free": True,
                                                          "address": i})
    print(result)
    print(result.status_code)
