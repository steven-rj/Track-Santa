#import statements
import requests
import json
import turtle

#create the Santa turtle object
santa = turtle.Turtle()


def setup(window):
    """
    DOCSTRING: creates the main window for the program
    """
    global santa

    window.setup(1000, 500)
    window.bgpic('earth.gif')
    window.setworldcoordinates(-180, -90, 180, 90)

    turtle.register_shape('santa.gif')
    santa.shape('santa.gif')


def move_santa(lat, long):
    """
    DOCSTRING: moves the Santa object to the given coordinates
    """
    global santa

    santa.penup()
    santa.goto(long, lat)
    santa.pendown()


def track_santa():
    """
    DOCSTRING: using open-notify's API, gets a JSON
               containing the ISS's position, and
               stores its latitude and longitude
               in respective vars.
               also prints error message if no response
               is received from the server.                
    """

    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        santa_info = json.loads(response.text)
        santa_position = santa_info["iss_position"]
        santa_lat = float(santa_position['latitude'])
        santa_lon = float(santa_position['longitude'])
        move_santa(santa_lat, santa_lon)
    else:
        print("North Pole, we have a problem:", response.status_code)

    widget = turtle.getcanvas()
    widget.after(5000, track_santa)


def main():
    """
    DOCSTRING: main function of the program
    """
    global santa

    screen = turtle.Screen()
    setup(screen)
    track_santa()


if __name__ == '__main__':
    main()
    turtle.mainloop()