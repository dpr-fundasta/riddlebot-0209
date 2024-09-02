import sqlite3
import random
import streamlit as st
# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect(r'\riddlebot\database\riddles.db')
    return conn

def add_riddle(question, correct_answer, reasoning_of_answer):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Insert the data into the table
    cursor.execute('''
        INSERT INTO riddles (question, correct_answer, reasoning_of_answer)
        VALUES (?, ?, ?);
    ''', (question, correct_answer, reasoning_of_answer))

    # Commit the changes to the database
    conn.commit()
    conn.close()

def fetch_random_riddle():
    st.session_state.qcount += 1
    conn = get_db_connection()
    cursor = conn.cursor()

    # Get the total number of rows in the table
    cursor.execute('SELECT COUNT(*) FROM riddles')
    row_count = cursor.fetchone()[0]
    
    if row_count == 0:
        conn.close()
        return None  # No data available

    # Get a random row number
    random_row_number = random.randint(0, row_count - 1)  # OFFSET starts at 0

    # Retrieve the random row from the table
    cursor.execute('''
        SELECT question, correct_answer, reasoning_of_answer
        FROM riddles
        LIMIT 1 OFFSET ?
    ''', (random_row_number,))

    # Fetch the result
    result = cursor.fetchone()
    conn.close()

    if result:
        # Return the result as a dictionary
        return {
            "question": result[0],
            "correct_answer": result[1],
            "reasoning_of_answer": result[2]
        }
    else:
        return None

# Example usage
# if __name__ == "__main__":
#     #add_riddle("What has to be broken before you can use it?", "Egg", "An egg must be broken before you can cook with it.")
#     riddle = fetch_random_riddle()
#     print(riddle)
