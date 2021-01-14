class Sort:
    def __init__(self,datas):
        self.datas = "".join([a.strip() for a in datas.splitlines()])

    def __repr__(self):
        return self.datas

    def get_dict(self) -> dict:
        return self.result()

    def result(self) -> dict:
        rules_sets = self.get_rules_sets(self.datas)
        resultat = {}

        for rule_set in rules_sets:
            for selector in self.get_selectors(rule_set):
                resultat[selector] = self.get_declaration_block(rule_set)

        return resultat

    def is_exeption(self, datas: str) -> bool:
        selectors = "".join(self.get_selectors(datas))
        return "@" in selectors

    def get_declaration_block(self, datas: str) -> list:
        if not self.is_exeption(datas):
            declaration_block = datas.split("{")[1]
            result = [elem.strip() for elem in declaration_block.split(";")]
        else:
            result = datas.split("{")[1]

        return result

    @staticmethod
    def get_rules_sets(datas: str) -> list:
        i: int = -1
        result: list = []
        temp: str = ""

        for data in datas:
            temp += data

            if data == "{":
                i += 1
            elif data == "}":
                if i == 0:
                    result.append(temp)
                    temp = ""
                i -= 1
        return result

    @staticmethod
    def get_selectors(datas: str) -> list:
        return datas.split("{")[0].split(",")
