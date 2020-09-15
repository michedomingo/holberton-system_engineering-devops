#!/usr/bin/python3
"""
Exports employee data into CSV
"""
if __name__ == '__main__':
    import csv
    import json
    import requests
    from sys import argv

    employee_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url + '/users/{}'.format(employee_id))
    employee = user.json().get('username')

    list = requests.get(url + '/todos', params={'userId': employee_id})
    list = list.json()

    employee = user.json().get('username')

    employee_dict = {}
    employee_dict[employee_id] = []

    for task in list:
        data = {}
        data['task'] = task.get('title')
        data['completed'] = task.get('completed')
        data['username'] = employee
        employee_dict[employee_id].append(data)

    with open('{}.json'.format(employee_id), 'w') as file:
        json.dump(employee_dict, file)
