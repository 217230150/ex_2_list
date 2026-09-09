participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]

scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]

qualification_score = 70
distinction_score = 90


# Helper: return the qualification label for a given score
def get_qualification(score):
    if score > distinction_score:
        return "DISTINCTION"
    elif score > qualification_score:
        return "QUALIFIED"
    else:
        return "NOT QUALIFIED"


# Make sure the lists have the same number of elements
if len(participants) != len(scores):
    print("Error: The participants and scores lists do not have the same number of elements.")
else:
    print(f"Verified: both lists have {len(participants)} elements.")


# First, display all the current participants with their scores. Use zip()
print("\n--- Current participants and their scores ---")
for name, score in zip(participants, scores):
    print(f"{name}: {score}")


# Write the logic to accept a new participant's name and their score.
# While entering, also check if they are already in the list of participants.
# If the participant is already registered, display a message and do not add them to the list.
# If the name is empty, then print an error saying that the name cannot be empty, and don't add them to the list.
# If the score is not a number, then print an error saying that the score must be a number, and don't add them to the list.
# If the score is less than 0 or greater than 100, then print an error saying that the score must be between 0 and 100, and don't add them to the list.
# Otherwise, add the participant and their score to the lists and display a message saying that they have been successfully registered.
new_name = input("\nEnter the name of the new participant: ").strip()

if new_name in participants:
    print(f"{new_name} is already registered, so they were not added.")
elif new_name == "":
    print("Error: The name cannot be empty.")
else:
    score_input = input(f"Enter the score for {new_name}: ").strip()
    try:
        new_score = int(score_input)
    except ValueError:
        print("Error: The score must be a number.")
    else:
        if new_score < 0 or new_score > 100:
            print("Error: The score must be between 0 and 100.")
        else:
            participants.append(new_name)
            scores.append(new_score)
            print(f"{new_name} has been successfully registered with a score of {new_score}.")


# Write the logic to search for a specific participant.
# If the participant is found, display their name, score, and whether they are qualified or not.
# If the score is more than the distinction score, display that they have a DISTINCTION.
# If the score is more than the qualification score, display that they are QUALIFIED.
# Otherwise, display that they are NOT QUALIFIED.
# If the participant is not found, display a message saying that they are not found.
search_name = input("\nEnter the name of the participant to search for: ").strip()

if search_name in participants:
    idx = participants.index(search_name)
    print(f"{search_name}: score {scores[idx]} ({get_qualification(scores[idx])})")
else:
    print(f"{search_name} was not found.")


# Display every participant's name, score, and whether they are qualified or not.
print("\n--- All participants ---")
for name, score in zip(participants, scores):
    print(f"{name}: {score} ({get_qualification(score)})")


# Write the logic to find if there's even one participant that has a distinction, and if all the participants have passed (i.e., scored 50 or more).
has_distinction = any(score > distinction_score for score in scores)
all_passed = all(score >= 50 for score in scores)
print(f"\nAt least one participant has a DISTINCTION: {has_distinction}")
print(f"All participants have passed (scored 50 or more): {all_passed}")


# Write the logic to update a participant's score.
# Ensure that the participant exists in the list before updating their score.
# Also ensure that the new score is a valid number between 0 and 100.
update_name = input("\nEnter the name of the participant whose score you want to update: ").strip()

if update_name not in participants:
    print(f"{update_name} was not found, so the score was not updated.")
else:
    score_input = input(f"Enter the new score for {update_name}: ").strip()
    try:
        new_score = int(score_input)
    except ValueError:
        print("Error: The score must be a number.")
    else:
        if new_score < 0 or new_score > 100:
            print("Error: The score must be between 0 and 100.")
        else:
            idx = participants.index(update_name)
            old_score = scores[idx]
            scores[idx] = new_score
            print(f"{update_name}'s score was updated from {old_score} to {new_score}.")


# Write the logic to withdraw (remove) a participant from the list.
# Ensure that the score for that specific participant is also removed from the scores list
withdraw_name = input("\nEnter the name of the participant to withdraw: ").strip()

if withdraw_name in participants:
    idx = participants.index(withdraw_name)
    removed_score = scores.pop(idx)
    participants.pop(idx)
    print(f"{withdraw_name} (score {removed_score}) was removed from the list.")
else:
    print(f"{withdraw_name} was not found, so nothing was removed.")


# Create and display a scoreboard where all the participants and their scores are displayed in descending order.
# Display their rank alongside the participant name and score
print("\n--- Scoreboard (descending order) ---")
ranked = sorted(zip(participants, scores), key=lambda item: item[1], reverse=True)
for rank, (name, score) in enumerate(ranked, start=1):
    print(f"Rank {rank}: {name} - {score}")


# Calculate statistics:
# Calculate what the highest score is, what lowest score is, what the average score is.
# Calculate how many participants have the highest score and the lowest score
# Calculate how many participants have distinctions, how many are qualified, and how many are not qualified
highest_score = max(scores)
lowest_score = min(scores)
average_score = sum(scores) / len(scores)
num_highest = scores.count(highest_score)
num_lowest = scores.count(lowest_score)
num_distinctions = sum(1 for score in scores if score > distinction_score)
num_qualified = sum(1 for score in scores if qualification_score < score <= distinction_score)
num_not_qualified = sum(1 for score in scores if score <= qualification_score)


# Generate a final report that displays the participant name, their rank, their score, and their qualification (DISTINCTION, QUALIFIED, NOT QUALIFIED)
# Also the display all the statistics you calculated above
print("\n=== FINAL REPORT ===")
ranked = sorted(zip(participants, scores), key=lambda item: item[1], reverse=True)
for rank, (name, score) in enumerate(ranked, start=1):
    print(f"Rank {rank}: {name} | Score: {score} | {get_qualification(score)}")

print("\n--- Statistics ---")
print(f"Highest score: {highest_score} (achieved by {num_highest} participant(s))")
print(f"Lowest score: {lowest_score} (achieved by {num_lowest} participant(s))")
print(f"Average score: {average_score:.2f}")
print(f"Number of participants with DISTINCTION: {num_distinctions}")
print(f"Number of QUALIFIED participants: {num_qualified}")
print(f"Number of NOT QUALIFIED participants: {num_not_qualified}")
