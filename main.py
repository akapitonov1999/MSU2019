# main.py -- put your code here!


class CellLine:
    cell_amount = 1
    global logged
    logged = []

    def __init__(self, name):
        self.name = name
        f = open(f'D:\\logs{self.name}.dat', 'a')
        logged.append(1)
        print(logged)

    def division_func(self, cell_amount):
        cell_amount = cell_amount * 2
        f = open(f'D:\\logs{self.name}.dat', 'a')
        logging_value = str(cell_amount) + '\n'
        f.write(logging_value)
        logged.append(cell_amount)
        return cell_amount

    def risk_func(self, cell_amount, risk=0.8):
        cell_amount = round(int(cell_amount) * risk)
        f = open(f'D:\\logs{self.name}.dat', 'a')
        logging_value = str(cell_amount) + '\n'
        f.write(logging_value)
        logged.append(cell_amount)
        return cell_amount

    def cycle(self):
        limit = 50
        i = 0
        print(logged)
        while i != limit:
            my_cells.division_func(cell_amount=logged[len(logged)-1])
            my_cells.risk_func(cell_amount=logged[len(logged)-1])
            i += 1

my_cells = CellLine('my cells')
my_cells.cycle()





