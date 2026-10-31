import pandas as pd

# Load data from CSV
df = pd.read_csv('food.csv')

# Function to display benefits and demerits
def display_food_info(food_item):
    if food_item in df['Food Item'].values:
        row = df[df['Food Item'] == food_item].iloc[0]

        print(f"Food Item: {row['Food Item']}")
        print(f"Benefits: {row['Benefits']}")
        print(f"Demerits: {row['Demerits']}")
    else:
        print("Food item not found!")

# Example usage
food_item = input("Enter a food item: ")
display_food_info(food_item)