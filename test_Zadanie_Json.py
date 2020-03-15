import unittest
from Zadanie_Json import get_data_users, get_data_posts, number_of_posts, unique_titles, closest_neighbour

class TestGetData(unittest.TestCase):
    def test_NumberOfPosts(self):
        self.assertListEqual(number_of_posts(get_data_posts("https://jsonplaceholder.typicode.com/posts"), get_data_users("https://jsonplaceholder.typicode.com/users")), [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) #OK
        users = [
            {
                "id": 1,
                "name": "Leanne Graham",
                "username": "Bret",
                "email": "Sincere@april.biz",
                "address": {
                    "street": "Kulas Light",
                    "suite": "Apt. 556",
                    "city": "Gwenborough",
                    "zipcode": "92998-3874",
                    "geo": {
                        "lat": "-37.3159",
                        "lng": "81.1496"
                    }
                },
                "phone": "1-770-736-8031 x56442",
                "website": "hildegard.org",
                "company": {
                    "name": "Romaguera-Crona",
                    "catchPhrase": "Multi-layered client-server neural-net",
                    "bs": "harness real-time e-markets"
                }
            },
            {
                "id": 2,
                "name": "Ervin Howell",
                "username": "Antonette",
                "email": "Shanna@melissa.tv",
                "address": {
                    "street": "Victor Plains",
                    "suite": "Suite 879",
                    "city": "Wisokyburgh",
                    "zipcode": "90566-7771",
                    "geo": {
                        "lat": "-43.9509",
                        "lng": "-34.4618"
                    }
                },
                "phone": "010-692-6593 x09125",
                "website": "anastasia.net",
                "company": {
                    "name": "Deckow-Crist",
                    "catchPhrase": "Proactive didactic contingency",
                    "bs": "synergize scalable supply-chains"
                }
            },
            {
                "id": 3,
                "name": "Clementine Bauch",
                "username": "Samantha",
                "email": "Nathan@yesenia.net",
                "address": {
                    "street": "Douglas Extension",
                    "suite": "Suite 847",
                    "city": "McKenziehaven",
                    "zipcode": "59590-4157",
                    "geo": {
                        "lat": "-68.6102",
                        "lng": "-47.0653"
                    }
                },
                "phone": "1-463-123-4447",
                "website": "ramiro.info",
                "company": {
                    "name": "Romaguera-Jacobson",
                    "catchPhrase": "Face to face bifurcated interface",
                    "bs": "e-enable strategic applications"
                }
            }
        ]
        posts = [
            {
                "userId": 1,
                "id": 1,
                "title": "title 1",
                "body": "body 1"
            },
            {
                "userId": 1,
                "id": 2,
                "title": "title 2",
                "body": "body 2"
            },
            {
                "userId": 2,
                "id": 3,
                "title": "title 3",
                "body": "body 3"
            },
            {
                "userId": 3,
                "id": 4,
                "title": "title 4",
                "body": "body 4"
            },
            {
                "userId": 3,
                "id": 5,
                "title": "title 5",
                "body": "body 5"
            }
        ]
        x = number_of_posts(posts, users)
        self.assertCountEqual(x, [2, 1, 2])

    def test_UniqueTitles(self):
        self.assertCountEqual(unique_titles(get_data_posts("https://jsonplaceholder.typicode.com/posts")), [])
        posts = [
            {
                "userId": 1,
                "id": 1,
                "title": "title 1",
                "body": "body 1"
            },
            {
                "userId": 1,
                "id": 2,
                "title": "title 3",
                "body": "body 2"
            },
            {
                "userId": 2,
                "id": 3,
                "title": "title 3",
                "body": "body 3"
            },
            {
                "userId": 3,
                "id": 4,
                "title": "title 3",
                "body": "body 4"
            },
            {
                "userId": 3,
                "id": 5,
                "title": "title 3",
                "body": "body 5"
            }
        ]
        self.assertListEqual(unique_titles(posts), ["title 3"])

    def test_ClosestNeighbour(self):
        self.assertListEqual(closest_neighbour(get_data_users("https://jsonplaceholder.typicode.com/users")), [4, 2, 1, 8, 9, 9, 4, 3, 3, 4]) #OK
        users = [
  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "60",
        "lng": "30"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
  },
  {
    "id": 2,
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    "address": {
      "street": "Victor Plains",
      "suite": "Suite 879",
      "city": "Wisokyburgh",
      "zipcode": "90566-7771",
      "geo": {
        "lat": "52",
        "lng": "41"
      }
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
      "name": "Deckow-Crist",
      "catchPhrase": "Proactive didactic contingency",
      "bs": "synergize scalable supply-chains"
    }
  },
  {
    "id": 3,
    "name": "Clementine Bauch",
    "username": "Samantha",
    "email": "Nathan@yesenia.net",
    "address": {
      "street": "Douglas Extension",
      "suite": "Suite 847",
      "city": "McKenziehaven",
      "zipcode": "59590-4157",
      "geo": {
        "lat": "50",
        "lng": "40"
      }
    },
    "phone": "1-463-123-4447",
    "website": "ramiro.info",
    "company": {
      "name": "Romaguera-Jacobson",
      "catchPhrase": "Face to face bifurcated interface",
      "bs": "e-enable strategic applications"
    }
  },
  {
    "id": 4,
    "name": "Patricia Lebsack",
    "username": "Karianne",
    "email": "Julianne.OConner@kory.org",
    "address": {
      "street": "Hoeger Mall",
      "suite": "Apt. 692",
      "city": "South Elvis",
      "zipcode": "53919-4257",
      "geo": {
        "lat": "30",
        "lng": "60"
      }
    },
    "phone": "493-170-9623 x156",
    "website": "kale.biz",
    "company": {
      "name": "Robel-Corkery",
      "catchPhrase": "Multi-tiered zero tolerance productivity",
      "bs": "transition cutting-edge web services"
    }
  },
  {
    "id": 5,
    "name": "Chelsey Dietrich",
    "username": "Kamren",
    "email": "Lucio_Hettinger@annie.ca",
    "address": {
      "street": "Skiles Walks",
      "suite": "Suite 351",
      "city": "Roscoeview",
      "zipcode": "33263",
      "geo": {
        "lat": "70",
        "lng": "40"
      }
    },
    "phone": "(254)954-1289",
    "website": "demarco.info",
    "company": {
      "name": "Keebler LLC",
      "catchPhrase": "User-centric fault-tolerant solution",
      "bs": "revolutionize end-to-end systems"
    }
  }
    ]
        self.assertListEqual(closest_neighbour(users), [1, 2, 1, 2, 0])

