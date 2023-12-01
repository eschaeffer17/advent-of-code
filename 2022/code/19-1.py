import re
from common import read_daily_input

class robot:
    def __init__(self, type: str, cost: dict, starting_num: int) -> None:
        self.type = type
        self.cost = cost
        self.num = starting_num

class ore_inventory:
    def __init__(self, type: str, inv: int) -> None:
        self.type = type
        self.inv = inv

def parse(blueprint: str):
    res: list[robot] = []
    for conf in blueprint.split(".")[:-1]:
        type = re.search("\w+(?=\s+robot)", conf)
        if type=='ore':
            starting_num=1
        else:
            starting_num=0
        cost_dict = {}
        costs = conf.split("costs ")[1]
        for i in costs.split(" and "):
            num, cost_type = i.split(" ")
            cost_dict[cost_type] = int(num)

        res.append(robot(type.group(),cost_dict, starting_num))

    return res


def compare_inventory(ore_type:str, robot_type:str):
    ore_inventory[]

# def build_robots():
#     robot('geode')


if __name__ == "__main__":
    input = read_daily_input('19-1')
    for blueprint in input:
        output = parse(blueprint)
        print(output)