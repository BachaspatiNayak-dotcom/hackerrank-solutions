"""
Problem: Captain's Room
Source: HackerRank

You are given K and a list of room numbers.
Each family room appears K times.
Captain's room appears once.
Find the Captain's room number.
"""

k = int(input())
rooms = list(map(int, input().split()))

print((k * sum(set(rooms)) - sum(rooms)) // (k - 1))