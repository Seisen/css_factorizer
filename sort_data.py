###temp
with open("test.txt") as f:
    inputs = f.read()


class Sort:
    def __init__(self,datas):
        self.datas = datas

    def __repr__(self):
        return self.run(self.datas)

    def run(self,datas) -> dict:
        result = {}

        rules_sets = self.get_rules_sets(datas)
        for rule_set in rules_sets:
            print(rule_set)
            selectors = self.get_selectors(rule_set)

            for selector in selectors:
                result[selector] = self.get_declaration_block(rule_set)

        return result

    @staticmethod
    def get_rules_sets(datas: str) -> list:
        return datas.replace("\n", "").split("}")

    @staticmethod
    def get_selectors(datas: str) -> list:
        selectors = datas.split("{")[0]
        return [elem.strip() for elem in selectors.split(",")]

    @staticmethod
    def get_declaration_block(datas: str) -> list:
        declaration_block = datas.split("{")[1]
        return [elem.strip() for elem in declaration_block.split(";")]
