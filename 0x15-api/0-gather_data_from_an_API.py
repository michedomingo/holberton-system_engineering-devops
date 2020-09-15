#!/usr/bin/python3
"""
For a given employee ID, returns information about their TODO list progress
"""
if __name__ == '__main__':
    import requests
    from sys import argv

    employee_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url + '/users', params={'id': employee_id})
    user = user.json()[0].get('name')

    list = requests.get(url + '/todos', params={'userId': employee_id})
    list = list.json()

    total = len(list)
    tasks = []

    for task in list:
        if task.get('completed') is True:
            tasks.append(task)

    print('Employee {} is done with tasks({}/{}):'
          .format(user, len(tasks), len(list)))

    for task in tasks:
        print('\t {}'.format(task.get('title')))
