var now = new Date();
var topic = "currentDateTime";var date = now.toISOString().slice(0, 10);
var time = now.toISOString().slice(11, 19);
var msg = {
    topic: topic,
    payload: {
        date: date,
        time: time
    }
};
msg.date = msg.payload.date;
msg.time = msg.payload.time;
msg.topic = topic;
return msg;
