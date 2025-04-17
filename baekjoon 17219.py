import sys
N, M = map(int, sys.stdin.readline().split())
site_dict = {}

for _ in range(N):
    site, password = sys.stdin.readline().strip().split()
    site_dict[site] = password

for _ in range(M):
    site = sys.stdin.readline().strip()
    print(site_dict[site])