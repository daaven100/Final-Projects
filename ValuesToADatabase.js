var query1 = "INSERT INTO pressure_data (date_collected, time_collected, tech_name, pressure_value, job_num, serial_num, notes) VALUES (" + msg.date + ", " + msg.time + ", “ + msg.customername + ”, “ + msg.analog + ", " + msg.jobnumber + ", " + msg.serialnumber + ”, ” + msg.description + “)";
msg.topic = "sql";
msg.payload = query1;
return msg;
