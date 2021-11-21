from requests import post

for i in range(1):
    result = post('http://127.0.0.1:5000/add/tenant', json={"id": "None",
                                                            "place_in_address": 1,
                                                            "place_in_room": 1,
                                                            "gender": True,
                                                            "age": 18,
                                                            "desire_communicate": True,
                                                            "vaccination_against_covid19": True,
                                                            "hasPet": False,
                                                            "hasChild": False,
                                                            "smoking": False,
                                                            "interests": []})
    print(result)
    print(result.status_code)
