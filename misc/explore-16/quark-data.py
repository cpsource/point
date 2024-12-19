import pandas as pd

def display_quark_data():
    # Define the chart data with nucleus weight and quark counts
    elements_quark_data = [
        {"Element": "Hydrogen", "NucleusWeight": 1, "UpQuarks": 2, "DownQuarks": 1},  # 1 proton
        {"Element": "Helium", "NucleusWeight": 4, "UpQuarks": 4, "DownQuarks": 4},  # 2 protons, 2 neutrons
        {"Element": "Carbon", "NucleusWeight": 12, "UpQuarks": 12, "DownQuarks": 12},  # 6 protons, 6 neutrons
        {"Element": "Oxygen", "NucleusWeight": 16, "UpQuarks": 16, "DownQuarks": 16},  # 8 protons, 8 neutrons
        {"Element": "Silicon", "NucleusWeight": 28, "UpQuarks": 28, "DownQuarks": 28},  # 14 protons, 14 neutrons
        {"Element": "Iron", "NucleusWeight": 56, "UpQuarks": 56, "DownQuarks": 56},  # 26 protons, 30 neutrons
        {"Element": "Sodium", "NucleusWeight": 23, "UpQuarks": 23, "DownQuarks": 23},  # 11 protons, 12 neutrons
        {"Element": "Lead", "NucleusWeight": 208, "UpQuarks": 208, "DownQuarks": 208},  # 82 protons, 126 neutrons
        {"Element": "Gold", "NucleusWeight": 197, "UpQuarks": 197, "DownQuarks": 197},  # 79 protons, 118 neutrons
        {"Element": "Uranium", "NucleusWeight": 238, "UpQuarks": 238, "DownQuarks": 238},  # 92 protons, 146 neutrons
    ]

    # Add total quarks for each element
    for element in elements_quark_data:
        element["TotalQuarks"] = element["UpQuarks"] + element["DownQuarks"]

    # Convert to DataFrame
    df_quarks = pd.DataFrame(elements_quark_data)

    # Display the data
    print("Quark Composition by Element")
    print(df_quarks)

# Call the function to display the data
if __name__ == "__main__":
    display_quark_data()

