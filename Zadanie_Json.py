import json
import urllib.request
import math


def get_data_posts():  # loads json from url, then creates the dictionary with post_data which I will be using lately
    url_posts = "https://jsonplaceholder.typicode.com/posts"
    response_posts = urllib.request.urlopen(url_posts)
    data_posts = json.loads(response_posts.read())
    return data_posts


def get_data_users():  # loads json from url, then creates the dictionary with user data which I will be using lately
    url_users = "https://jsonplaceholder.typicode.com/users"
    response_users = urllib.request.urlopen(url_users)
    data_users = json.loads(response_users.read())
    return data_users


def zerolist(n):  # creates 1-dimensional matrix filled with zeros
    zeros = [0] * n
    return zeros


def number_of_posts(data_posts, data_users):  # counts number of posts created per user, then prints statistics
    number_of_posts = zerolist(len(data_users))

    for i in range(0, len(data_posts)):
        post = data_posts[i]['userId']
        number_of_posts[post - 1] = number_of_posts[post - 1] + 1

    for i in range(0, len(data_users)):
        print(data_users[i]['name'] + ' napisal(a) ' + str(number_of_posts[i]) + ' postow!')


def unique_titles(data_posts):  # checks whether title of the post is unique. If so, adds title to the list
    titles = zerolist(len(data_posts))

    for i in range(0, len(data_posts)):
        titles[i] = data_posts[i]['title']

    unique = []
    counter = 0

    for i in range(0, len(data_posts)):
        title = titles[i]
        for j in range(0, len(data_posts)):
            if title == titles[j]:
                counter = counter + 1
        if counter != 1:
            unique.append(title)
        counter = 0

    return unique


def print_unique(unique):  # prints list of the unique titles. If the list is empty function informs that all of the
    # titles are unique
    if len(unique) == 0:
        print('Wszystkie tytuły postow są unikalne!')
    else:
        for i in range(0, len(unique)):
            print(unique[i])


def generate_square_matrix(data_users):  # generates square matrix with len(data_users) rows and columns
    matrix = [[0 for x in range(len(data_users))] for y in range(len(data_users))]
    return matrix


def closest_neighbour(data_users):  # compares latitude and longitude of every user to find closest-living forum user
    # function implements Haversine formula to determine the great-circle distance between two points on a sphere

    # required matrixes and Earts's radius in metres
    latitude = []
    longitude = []
    delta_latitude = generate_square_matrix(data_users)
    delta_longitude = generate_square_matrix(data_users)
    radius = 6371000  # metres
    a = generate_square_matrix(data_users)
    c = generate_square_matrix(data_users)
    d = generate_square_matrix(data_users)
    minimal = []

    # appending latitude and longitude of every user, then converts degrees into radians
    for i in range(0, len(data_users)):
        latitude.append(data_users[i]['address']['geo']['lat'])
        longitude.append(data_users[i]['address']['geo']['lng'])
        latitude[i] = math.radians(float(latitude[i]))
        longitude[i] = math.radians(float(longitude[i]))

    # counting difference between two latitues and longitudes, then applying Haversine formula and looking for the
    # closest neighbours' index (user ID in this case). At last printing out closest neighbours
    for i in range(0, len(data_users)):
        for j in range(0, len(data_users)):
            # I am aware that there are going to be zeros on the diagonal, will take care of that later
            delta_latitude[i][j] = math.fabs(float(latitude[i]) - float(latitude[j]))
            delta_longitude[i][j] = math.fabs(float(longitude[i]) - float(longitude[j]))
            a[i][j] = math.pow(math.sin(delta_latitude[i][j] / 2), 2) + math.cos(latitude[i]) * math.cos(
                latitude[j]) * math.pow(math.sin(delta_longitude[i][j] / 2), 2)
            c[i][j] = 2 * math.atan2(math.sqrt(a[i][j]), math.sqrt(1 - a[i][j]))
            d[i][j] = (c[i][j] * radius) / 1000  # dividing by 1000 to convert the distance from metres to kilometres
        d[i][i] = 40075  # swapping zeros on diagonal for circuit of Earth - prohibitive value of distance
    # printing user ID of closest neighbour
    for i in range(0, len(data_users)):
        minimal.append(d[i].index(min(d[i])))
        print(str(i + 1) + ' jest najblizej od ' + str(minimal[i] + 1))


# task 1
data_posts = get_data_posts()
data_users = get_data_users()
# task 2
number_of_posts(data_posts, data_users)
print('\n')
# task 3
unique = unique_titles(data_posts)
print_unique(unique)
print('\n')
# task 4
closest_neighbour(data_users)
