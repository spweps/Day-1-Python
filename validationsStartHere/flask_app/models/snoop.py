from flask import flash
import re


class Snoop:

    @staticmethod
    def validate_victim(victim):
        email_regex = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$')
        social_regex = re.compile(r'^\d{3}-\d{2}-\d{4}$')
        is_valid = True
        
        if len(victim["fullname"]) < 1:
            flash("A real full name please")
            is_valid = False
        if not email_regex.match(victim["email"]) < 1:
            flash("Invalid email, try again")
            is_valid = False
        if len(victim["maiden"]) < 1:
            flash("Mother's maiden name required")
            is_valid = False
        if not social_regex.match(victim["social"]) < 1:
            flash("Invalid social, are you even a citizen?")
            is_valid = False
        if "trash" not in victim:
            flash("We need your trash")
            is_valid = False
        
        return is_valid