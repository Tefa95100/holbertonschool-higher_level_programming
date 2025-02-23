#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    link = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(link)

    print("Status code: {}".format(response.status_code))

    if response.status_code == 200:
        data = response.json()
        print(word["title"] for word in data)
    else:
        print("Failled request")


def fetch_and_save_posts():
    link = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(link)
    file_csv = "posts.csv"

    if response.status_code == 200:
        data = response.json()
        dict_data = [{"id": word["id"], "title": word["title"],
                      "body": word["body"]} for word in data]

        with open(file_csv, "w", newline="", encoding="utf-8") as csvfile:
            field_name = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=field_name)
            writer.writeheader()
            writer.writerows(dict_data)

        print("Success saved to posts.csv")
    else:
        print("Failed to retrieve posts")
