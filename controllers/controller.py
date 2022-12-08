from flask import render_template, request, redirect # ADDED
from app import app
from models.event_list import events
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['POST'])
def create():
    # print(request.form)
    description = request.form['description']
    date = request.form['date']
    event_name = request.form['event']
    number_of_guests = request.form['num_guests']
    room_location = request.form['room']
    new_event = Event(date, event_name, number_of_guests, room_location, description)
    # rec = False
    recurring = ""
    recurring = request.form['rec']
    # print(recurring)
    if recurring == "on":
        new_event.recurring()
        events.append(new_event)
        return redirect('/events')

        # print(rec)
    else: 
        pass
    
    events.append(new_event)
    return redirect('/events')

