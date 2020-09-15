#!/usr/bin/python3
"""
Script that exports task 1 to csv
"""
if __name__ == '__main__':
    import csv
    import requests
    from sys import argv

    employee_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url + '/users/{}'.format(employee_id))

    list = requests.get(url + '/todos', params={'userId': employee_id})
    list = list.json()

    employee = user.json().get('username')

    with open('{}.csv'.format(employee_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in list:
            status = task['completed']
            title = task['title']
            writer.writerow(['{}'.format(employee_id),
                             '{}'.format(employee),
                             '{}'.format(status),
                             '{}'.format(title)])
