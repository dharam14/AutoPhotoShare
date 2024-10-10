def first_log(log_file):
    from datetime import datetime
    with open(log_file,'a') as f:
        current_time = datetime.now()
        formatted_time = current_time.strftime(" %Y-%m-%d  %H:%M:%S  ")
        f.write(formatted_time + "Operation started"+"\n\n")
        f.write("-----DETAILS OF OPERATIONS-----"+"\n\n")

def write_to_log(message, log_file):
    from datetime import datetime
    with open(log_file, "a") as f:
        current_time = datetime.now()
        formatted_time = current_time.strftime(" %Y-%m-%d  %H:%M:%S  ")
        modified_message = formatted_time + message
        f.write(modified_message + "\n")    