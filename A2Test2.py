# Martin Sergo
# A2 2750 W24
import Physics


def write_table_to_files(table):

    if type(table) != Physics.Table:
        print('invalid type')
        return
    i = 0
    if table:
        with open(f'table-{i}.svg', 'w') as file:
                    file.write(table.svg())
    while (table):
        i += 1
        file_name = f'table-{i}.svg'
        table = table.segment()
        if table:
            with open(file_name, 'w') as file:
                file.write(table.svg())
    return

def main():
    # Import user created pics library
    import math
    import Physics as p

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

    write_table_to_files(table)
    return

if __name__ == "__main__":
    main()