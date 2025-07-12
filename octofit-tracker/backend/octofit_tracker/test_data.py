# Test data for populating octofit_db
TEST_USERS = [
    {"email": "alice@example.com", "name": "Alice", "password": "alicepass"},
    {"email": "bob@example.com", "name": "Bob", "password": "bobpass"},
    {"email": "carol@example.com", "name": "Carol", "password": "carolpass"}
]

TEST_TEAMS = [
    {"name": "Team Alpha", "members": ["alice@example.com", "bob@example.com"]},
    {"name": "Team Beta", "members": ["carol@example.com"]}
]

TEST_ACTIVITIES = [
    {"user_email": "alice@example.com", "activity_type": "run", "duration": 30, "date": "2025-07-12T08:00:00Z"},
    {"user_email": "bob@example.com", "activity_type": "walk", "duration": 45, "date": "2025-07-12T09:00:00Z"},
    {"user_email": "carol@example.com", "activity_type": "cycle", "duration": 60, "date": "2025-07-12T10:00:00Z"}
]

TEST_LEADERBOARD = [
    {"team_name": "Team Alpha", "points": 100},
    {"team_name": "Team Beta", "points": 80}
]

TEST_WORKOUTS = [
    {"name": "Pushups", "description": "Do 20 pushups"},
    {"name": "Situps", "description": "Do 30 situps"}
]
