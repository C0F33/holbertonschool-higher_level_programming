#!/usr/bin/python3
import requests
import json
import csv


def fetch_and_print_posts():
    """Fetch and print the first 10 posts from a given URL"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))
        print(f'Status Code: {response.status_code}')
    else:
        print(f'Request failed with status code: {response.status_code}')


def fetch_and_save_posts():
    """Fetch and save the first 10 posts from a given URL"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        posts_to_save = [{'id': post['id'], 'title': post['title'],
                          'body': post['body']} for post in posts]
        with open('posts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_to_save)
    else:
        print(f'Request failed with status code: {response.status_code}')
