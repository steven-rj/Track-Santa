import requests
import json
import turtle

santa = turtle.Turtle()


def setup(window):
    global santa

    window.setup(1000, 500)
    window.bgpic('earth.gif')
    window.setworldcoordinates(-180, -90, 180, 90)

    turtle.register_shape('santa.gif')
    santa.shape('santa.gif')


def move_santa(lat, long):
    global santa

    santa.penup()
    santa.goto(long, lat)
    santa.pendown()


def track_santa():

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
    global santa

    screen = turtle.Screen()
    setup(screen)
    track_santa()


if __name__ == '__main__':
    main()
    turtle.mainloop()