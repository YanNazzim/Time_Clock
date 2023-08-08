import datetime
import json

class Punches:
    def __init__(self):
        self.users = {}
        self.punch_records = {}
        self.load_users()
    
    def display_logs(self):
        try:
            with open("punches.txt", "r") as file:
                logs = file.read()
                print(logs)
        except FileNotFoundError:
            print("Log file not found.")

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {}

    def save_users(self):
        with open("users.json", "w") as file:
            json.dump(self.users, file)

    def add_user(self, user_id, user_name):
        self.users[user_id] = user_name
        self.save_users()


    def remove_user(self, user_id):
        if user_id in self.users:
            user_name = self.users[user_id]
            del self.users[user_id]
            if user_id in self.punch_records:
                del self.punch_records[user_id]
            print(f"User with ID {user_id} ({user_name}) has been removed.")
        else:
            print("User not found.")
        
        
    def print_current_users(self):
        if self.users:
            print("Current users:")
            for user_id, user_name in self.users.items():
                print(f"User ID: {user_id}, Name: {user_name}\n")
        else:
            print(f"No users in the system.\n")

    def clock_in(self, user_id):
        if user_id in self.users:
            if self.punch_records.get(user_id) and self.punch_records[user_id]['clock_in'] is not None:
                print(f"{self.users[user_id]} has already clocked in.")
            else:
                current_time = datetime.datetime.now()
                self.punch_records.setdefault(user_id, {'clock_in': None, 'clock_out': None, 'session_start': None})
                self.punch_records[user_id]['clock_in'] = current_time
                self.punch_records[user_id]['session_start'] = current_time
                self._write_punch_record(user_id, current_time, "Clock In")
                print(f"Hello, {self.users[user_id]}! You've clocked in at {current_time.strftime('%I:%M %p')}\n")
        else:
            print("User not found.")

    def clock_out(self, user_id):
        if user_id in self.users and user_id in self.punch_records and self.punch_records[user_id]['clock_out'] is None:
            current_time = datetime.datetime.now()
            session_start_time = self.punch_records[user_id]['session_start']
            if session_start_time:
                session_duration = current_time - session_start_time
                self.punch_records[user_id]['session_start'] = None
            else:
                session_duration = datetime.timedelta(seconds=0)
    
            self.punch_records[user_id]['clock_out'] = current_time
            self._write_punch_record(user_id, current_time, "Clock Out")
            formatted_duration = self.format_duration(session_duration)
            print(f"Goodbye, {self.users[user_id]}! You've clocked out at {current_time.strftime('%I:%M:%S %p')}")
            print(f"Session duration: {formatted_duration}")
            return formatted_duration
        else:
            print("User not found or already clocked out.")
            return None
    
    def format_duration(self, duration):
        hours, remainder = divmod(duration.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours} hours {minutes} minutes {seconds} seconds"
    def get_total_time(self):
        total_time_seconds = 0

        for user_id, punch_record in self.punch_records.items():
            clock_in_time = punch_record['clock_in']
            clock_out_time = punch_record['clock_out']

            if clock_in_time and clock_out_time:
                session_duration = clock_out_time - clock_in_time
                total_time_seconds += session_duration.total_seconds()

        total_time = datetime.timedelta(seconds=total_time_seconds)
        formatted_total_time = self.format_duration(total_time)
        return formatted_total_time


    
    def _write_punch_record(self, user_id, Timestamp, action):
        current_time = datetime.datetime.now()
        current_time_str = current_time.strftime("%I:%M:%S %p")  # Format time as 12-hour with AM/PM and seconds
        current_date_str = current_time.strftime("%Y-%m-%d")  # Format date as YYYY-MM-DD
        if user_id in self.users:
            user_name = self.users[user_id]
        else:
            user_name = "Unknown User"

        with open("punches.txt", "a") as file:
            file.write(f"User ID: {user_id}, Name: {user_name}, Action: {action}, Date: {current_date_str} Time: {current_time_str}\n")
