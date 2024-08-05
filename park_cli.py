from park_collection import ParkCollection
import json

def park_cli():
    with open("nps.json", 'r') as nps:
        nps_json = json.load(nps)
        park_list = ParkCollection(nps_json)
        while True:
            correct = 0
            wrong = 0
            display_menu()
            try:
                choice = input("Choose 1, 2, or 3: ")
                if choice == "1":
                    park_name = input("Enter the park name: ")
                    park = next((p for p in park_list.parks if p.fullName == park_name), None)
                    if park:
                        print("\nPark Information:")
                        print("Name:", park.fullName)
                        print("Location:", park.location)
                        print("Park Code:", park.code)
                        print("Total Amenities:", park.total_activities())
                        print("Total Topics:", park.total_topics())
                        print("Latitude and Longitude:", park.latitude_longitude())
                    else:
                        print("Park not found.")
                if choice == "2":
                    user_choice1 = input("What park has the most total activities?: ")
                    most_activities_park = park_list.most_activities()
                    if user_choice1 == most_activities_park:
                        correct += 1
                        print("Correct!")
                    else:
                        wrong += 1
                        print("Wrong!, the correct answer is", most_activities_park)
                    user_choice2 = input("What park has the most topics: ")
                    most_topics_park = park_list.most_topics()
                    if user_choice2 == most_topics_park:
                        correct += 1
                        print("Correct!")
                    else:
                        wrong += 1
                        print("Wrong!, the correct answer is", most_topics_park)
                    user_choice3 = input("What is the total amount of parks in the JSON: ")
                    total_parks = park_list.len_park_list()
                    if user_choice3 == total_parks or user_choice3 == "5":
                        correct += 1
                        print("Correct!")

                    else:
                        wrong += 1
                        print("Wrong!, the correct answer is", total_parks)
                        print("Correct:")
                    print("You have", correct, "correct answers out of 3")
                    print((float(correct/3)*100), "%")
                    #change to multiply by 100(from code review)
                if choice == "3":
                    print("Goodbye")
                    break
            except ValueError:
                print("Invalid Input, user must enter a number being 1, 2, or 3")
def display_menu():
    print("\nGame Menu:")
    print("1. Display Park Information")
    print("2. Start the Quiz")
    print("3. Quit")

if __name__ == "__main__":
    park_cli()