"""This module is supposed to produce and present a simple text based 
diagram (maybe graphic) about the results."""

def create(prog_languages: dict):
    cur = ""
    all = sum(list(prog_languages.values()))
    pros = None
    for a, b in prog_languages.items():
        pros = (b*100//all)
        cur = "|"*pros
        print(f"{a:<10}{cur:<40}{pros}%")

