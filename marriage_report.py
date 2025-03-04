"""
Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""
import os
import sqlite3
import pandas as pd
from create_relationships import db_path, script_dir

def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()
    print(married_couples)
    # Save all married couples to CSV file
    csv_path = os.path.join(script_dir, 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)

def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    # TODO: Function body
    # Hint: See example code in lab instructions entitled "Get a List of Relationships"

    married_couples_query = """
    SELECT person1.name, person2.name, start_date, type FROM relationships
    JOIN people person1 ON person1_id = person1.id
    JOIN people person2 ON person2_id = person2.id
    WHERE type = "spouse";
    """
    cursor.execute(married_couples_query)
    married_couples = cursor.fetchall()
    con.close() 
    return married_couples


def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """

    # TODO: Function body
    # Hint: We did this in Lab 7.
    data = []
    for name1, name2, anniversary, type in married_couples:
        data.append({'Name1' : name1, 'name2' : name2, 'Anniversary' : anniversary})
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)

if __name__ == '__main__':
   main()






