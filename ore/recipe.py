class recipe(object):
    def __init__(self, name, tag, req_dict, out_dict):
        self.name = name
        self.tag = tag
        self.req_dict = req_dict
        self.out_dict = out_dict

    def req_line(self):
        line = ""
        for i in self.req_dict:
            if self.req_dict[i] != 0:
                line += i + "=" + str(self.req_dict[i]) + ", "
        return line

    def out_line(self):
        line = ""
        for i in self.out_dict:
            if self.out_dict[i] != 0:
                line += i + "=" + str(self.out_dict[i]) + ", "
        return line


def res_dict(copper_ore=0, tin_ore=0, bronze_ore=0, undefined_ore=0):
    resource_dict = {COPPER_ORE: copper_ore, TIN_ORE: tin_ore, BRONZE_INGOT: bronze_ore, UNDEFINED_ORE: undefined_ore}
    return resource_dict


USER_ID = "user_id"
NAME = "name"
GUILD_ID = "guild_id"
COPPER_ORE = "Медная руда"  # 3
TIN_ORE = "Оловянная руда"  # 4
BRONZE_INGOT = "Бронзовая руда"  # 5
UNDEFINED_ORE = "Неопределенная руда"  # 6

res_keys_dict = {COPPER_ORE: "item_№1", TIN_ORE: "item_№2", BRONZE_INGOT: "item_№3", UNDEFINED_ORE: "item_№4"}
res_emoji_id = {BRONZE_INGOT: 747215265573503018}

recipes_dict = {BRONZE_INGOT: recipe(name=BRONZE_INGOT, tag="BRZ", req_dict=res_dict(copper_ore=2, tin_ore=1),
                                     out_dict=res_dict(bronze_ore=1))}


def get_recipe(num=None, name=None, tag=None):
    result = None

    if num is not None:
        j = 0
        for i in recipes_dict:
            j += 1
            if j == num:
                result = recipes_dict[i]

    if name is not None:
        for i in recipes_dict:
            if recipes_dict[i].name == name:
                result = recipes_dict[i]

    if tag is not None:
        for i in recipes_dict:
            if recipes_dict[i].tag == tag:
                result = recipes_dict[i]

    return result
