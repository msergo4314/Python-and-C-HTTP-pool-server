# Martin Sergo
# A2 2750 W24

def main():
    # Import user created physics library
    import math
    import Physics as p
    # from start import setup
    
    # setup()
    table = p.Table()
    pos = p.Coordinate(p.TABLE_WIDTH / 2.0 - math.sqrt(p.BALL_DIAMETER * p.BALL_DIAMETER / 2.0),\
    p.TABLE_WIDTH / 2.0 - math.sqrt(p.BALL_DIAMETER * p.BALL_DIAMETER / 2.0))
    sb = p.StillBall(1, pos) #create new still ball with a position and number
    
    pos, vel, acc = p.Coordinate(p.TABLE_WIDTH / 2.0, p.TABLE_LENGTH - p.TABLE_WIDTH / 2.0),\
    p.Coordinate(0.0, -1000.0),\
    p.Coordinate(0.0, 180.0)
    
    rb = p.RollingBall(0, pos, vel, acc)
    table += sb
    table += rb
    print(table)

    while table:
        table = table.segment()
        print(table)
    return

if __name__ == "__main__":
    main()