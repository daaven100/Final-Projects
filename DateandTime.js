//This code was used in my Digital Pressure Recorder Project to format the current date and time in the Node-RED software
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
