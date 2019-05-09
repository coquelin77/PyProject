#from  traffic import Vehicle
import traffic


if __name__ == '__main__':


    c = traffic.Vehicle(23, 23)

    c.move()

    c.speedUp(22)

    c.move()

    c.speedDown(21)

    c.move()

    c.setSpeed(60)

    c.move()

    c.speedDown(100)

    c.move()