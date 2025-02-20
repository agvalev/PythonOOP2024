class Player:
    def __init__(self, name, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict[str, int] = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return (f"Skill {skill_name} added to the "
                f"collection of the player {self.name}")

    def player_info(self) -> str:
        result = (f"Name: {self.name}\n"
                f"Guild: {self.guild}\n"
                f"HP: {self.hp}\n"
                f"MP: {self.mp}\n")
        formated_skills = [
            f"==={skill} - {mana}"
            for skill, mana in self.skills.items()
        ]
        result += "\n".join(formated_skills)
        return result
