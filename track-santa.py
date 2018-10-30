import requests
import json
import turtle

iss = turtle.Turtle()


def setup(window):
    global iss

    window.setup(1000, 500)
    window.bgpic('earth.gif')
    window.setworldcoordinates(-180, -90, 180, 90)

    turtle.register_shape('iss.gif')
    iss.shape('iss.gif')


def move_iss(lat, long):
    global iss

    iss.penup()
    iss.goto(long, lat)
    iss.pendown()


def track_iss():

    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)

    if response.status_code == 200:
        iss_info = json.loads(response.text)
        iss_position = iss_info["iss_position"]
        iss_lat = float(iss_position['latitude'])
        iss_lon = float(iss_position['longitude'])
        move_iss(iss_lat, iss_lon)
    else:
        print("Houston, we have a problem:", response.status_code)

    widget = turtle.getcanvas()
    widget.after(5000, track_iss)


def main():
    global iss

    screen = turtle.Screen()
    setup(screen)
    track_iss()


if __name__ == '__main__':
    main()
    turtle.mainloop()