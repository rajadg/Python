

import os


def execute():
    os.remove("D:\\Temp\\Python\\employees.db")
    import tables
    import create_tables
    import add_entries_session
    import update_entries_session
    import query_entries_session
    
    
execute()

