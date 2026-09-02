# ==========================================
# Day 25 - GitHub Profile Analyzer
# 30 Days Python GitHub Project Challenge
# ==========================================

import requests


print("======================================")
print("         GITHUB PROFILE ANALYZER")
print("======================================")


# ==========================================
# GitHub API
# ==========================================

BASE_URL = "https://api.github.com/users"


# ==========================================
# Get Username
# ==========================================

username = input("\nEnter GitHub username: ").strip()

if username == "":
    print("❌ Username cannot be empty.")
    exit()


# ==========================================
# Get User Data
# ==========================================

try:

    response = requests.get(
        f"{BASE_URL}/{username}",
        timeout=10
    )

    data = response.json()

except requests.exceptions.RequestException:

    print("\n❌ Internet connection error.")
    exit()


# ==========================================
# Check Response
# ==========================================

if response.status_code != 200:

    print("\n❌ GitHub profile not found.")

    if "message" in data:
        print("Reason:", data["message"])

    exit()


# ==========================================
# Extract Profile Information
# ==========================================

name = data.get("name") or "Not Available"

bio = data.get("bio") or "No bio available"

location = data.get("location") or "Not Available"

company = data.get("company") or "Not Available"

public_repos = data.get("public_repos", 0)

followers = data.get("followers", 0)

following = data.get("following", 0)

created_at = data.get("created_at", "Not Available")

profile_url = data.get("html_url", "Not Available")

avatar_url = data.get("avatar_url", "Not Available")


# ==========================================
# Get Repository Data
# ==========================================

try:

    repo_response = requests.get(
        f"{BASE_URL}/{username}/repos",
        params={
            "per_page": 100,
            "sort": "stars"
        },
        timeout=10
    )

    repositories = repo_response.json()

except requests.exceptions.RequestException:

    repositories = []


# ==========================================
# Analyze Repositories
# ==========================================

total_stars = 0
total_forks = 0

top_repository = None

if isinstance(repositories, list):

    for repo in repositories:

        stars = repo.get("stargazers_count", 0)
        forks = repo.get("forks_count", 0)

        total_stars += stars
        total_forks += forks

        if top_repository is None:
            top_repository = repo

        elif stars > top_repository.get(
            "stargazers_count", 0
        ):
            top_repository = repo


# ==========================================
# Display Profile
# ==========================================

print("\n======================================")
print("          GITHUB PROFILE")
print("======================================")

print(f"Username       : {data.get('login')}")
print(f"Name           : {name}")
print(f"Bio            : {bio}")
print(f"Location       : {location}")
print(f"Company        : {company}")

print("--------------------------------------")

print(f"Public Repos   : {public_repos}")
print(f"Followers      : {followers}")
print(f"Following      : {following}")

print("--------------------------------------")

print(f"Total Stars    : {total_stars}")
print(f"Total Forks    : {total_forks}")

print("--------------------------------------")

print(f"Created At     : {created_at}")
print(f"Profile URL    : {profile_url}")
print(f"Avatar URL     : {avatar_url}")


# ==========================================
# Top Repository
# ==========================================

if top_repository:

    print("\n======================================")
    print("         TOP REPOSITORY")
    print("======================================")

    print(f"Name           : {top_repository.get('name')}")
    print(
        f"Stars          : "
        f"{top_repository.get('stargazers_count', 0)}"
    )
    print(
        f"Forks          : "
        f"{top_repository.get('forks_count', 0)}"
    )
    print(
        f"Language       : "
        f"{top_repository.get('language') or 'Not Available'}"
    )
    print(
        f"URL            : "
        f"{top_repository.get('html_url')}"
    )


# ==========================================
# Simple Analysis
# ==========================================

print("\n======================================")
print("         PROFILE ANALYSIS")
print("======================================")


if followers >= 1000:
    print("Followers      : ⭐ Popular Profile")

elif followers >= 100:
    print("Followers      : 👍 Growing Profile")

else:
    print("Followers      : 🌱 Beginner Profile")


if public_repos >= 20:
    print("Repositories   : 🚀 Strong Project Activity")

elif public_repos >= 5:
    print("Repositories   : 👍 Good Project Activity")

else:
    print("Repositories   : 🌱 Keep Building")


if total_stars >= 100:
    print("Stars          : 🏆 Excellent Community Reach")

elif total_stars >= 10:
    print("Stars          : ⭐ Good Community Reach")

else:
    print("Stars          : 💪 Keep Sharing Projects")


print("======================================")
print("      ANALYSIS COMPLETED! 🎉")
print("======================================")