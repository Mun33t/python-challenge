# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os
import numpy
import pandas

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
net_changes = []  

# Initialize net_changes as a    list
greatest_increase = ["", 0]  # Month and amount
greatest_decrease = ["", 0]  # Month and amount

# Add more variables to track other necessary financial data


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1

    # Track the total and net change
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        total_net += int(row[1])  # Convert to int

        # Track the net change
        net_change = int(row[1]) - previous_net  # Calculate the change
        net_changes.append(net_change)  # Append the change
        previous_net = int(row[1])  # Update previous_net

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase = [row[0], net_change]

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease = [row[0], net_change]

# Calculate the average net change across the months
if len(net_changes) > 0:
    average_net_change = sum(net_changes) / len(net_changes)
else:
    average_net_change = 0


# Calculate the average net change across the months
if len(net_changes) > 0:
    average_net_change = sum(net_changes) / len(net_changes)
else:
    average_net_change = 0

# Generate the output summary
output = (
    f"\nFinancial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_net_change:.2f}\n"
    f"Greatest Increase in Profit: {greatest_increase[0]}(${greatest_increase[1]})\n"
    f"Greatest Decrease in Profit: {greatest_decrease[0]}(${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)