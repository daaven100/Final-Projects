msg.payload = {
        job_number: msg.jobnumber,
        serial_number: msg.serialnumber,
        test_pressure: msg.analog,
        description: msg.description,
        customer_name: msg.customername,
        date: msg.date,
        time: msg.time
    };
    return msg;