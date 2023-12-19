from typing import Optional
from util import getlines

data = getlines("19")
data = getlines("19s")


class Range:
    mins = {"x": 1, "m": 1, "a": 1, "s": 1}
    maxs = {"x": 4000, "m": 4000, "a": 4000, "s": 4000}

    def __init__(self, other=None):
        if other is not None:
            self.mins = other.mins.copy()
            self.maxs = other.maxs.copy()

    def score(self):
        res = 1
        for c in "xmas":
            res *= self.maxs[c] - self.mins[c] + 1
        return res

    def __str__(self) -> str:
        return f"x: {self.mins['x']} - {self.maxs['x']}, m: {self.mins['m']} - {self.maxs['m']}, a: {self.mins['a']} - {self.maxs['a']}, s: {self.mins['s']} - {self.maxs['s']}"


class Rule:
    operator: Optional[str]
    field: Optional[str]
    cmp: Optional[int]
    result: str

    def __init__(self, rulestr: str):
        self.operator = None
        self.field = None
        self.cmp = None
        if ":" not in rulestr:
            self.result = rulestr
        else:
            cond, dest = rulestr.split(":")
            self.operator = cond[1]
            self.field = cond[0]
            self.cmp = int(cond[2:])
            self.result = dest

    # part 1
    def eval(self, widget):
        if self.operator is None:
            return self.result
        elif self.operator == "<":
            return self.result if widget[self.field] < self.cmp else None
        elif self.operator == ">":
            return self.result if widget[self.field] > self.cmp else None
        print(f"BAD RULE {self.__dict__}")
        return None

    # part 2
    def splitrange(self, range):
        if self.operator is None:
            return range, None
        if self.operator == "<":
            if self.cmp <= range.mins[self.field]:
                return None, range
            if self.cmp > range.maxs[self.field]:
                return range, None
            passrange = Range(range)
            failrange = Range(range)
            passrange.maxs[self.field] = self.cmp - 1
            failrange.mins[self.field] = self.cmp
            return passrange, failrange
        else:
            if self.cmp >= range.maxs[self.field]:
                return None, range
            if self.cmp < range.mins[self.field]:
                return range, None
            passrange = Range(range)
            failrange = Range(range)
            passrange.mins[self.field] = self.cmp + 1
            failrange.maxs[self.field] = self.cmp
            return passrange, failrange


####### Part 1 ###########


def evaluate_widget(widget, workflows):
    current_workflow = "in"
    while current_workflow not in ["A", "R"]:
        for rule in workflows[current_workflow]:
            current_workflow = rule.eval(widget)
            if current_workflow:
                break
    return current_workflow


def make_widget(row):
    res = {}
    for assignment in row[1:-1].split(","):
        var, val = assignment.split("=")
        res[var] = int(val)
    return res


workflows = {}
res = 0
for row in data:
    if row[0] == "{":
        widget = make_widget(row)
        if evaluate_widget(widget, workflows) == "A":
            res += sum(widget.values())
    else:
        label, rules = row[:-1].split("{")
        parsed_rules = [Rule(rule) for rule in rules.split(",")]
        workflows[label] = parsed_rules
print(res)

####### Part 2 ###########


def get_destinations(range, workflow):
    range_to_dest = {}
    for rule in workflow:
        passrange, range = rule.splitrange(range)
        if passrange is not None:
            range_to_dest[passrange] = rule.result
        if range is None:
            return range_to_dest


def get_results(workflows):
    current_workflows = {Range(): "in"}
    res = 0
    while len(current_workflows) > 0:
        next_workflows = {}
        for range, workflow_id in current_workflows.items():
            if workflow_id == "A":
                res += range.score()
                print(f"Accepting {range} for {range.score()}")
            elif workflow_id != "R":
                next_workflows.update(get_destinations(range, workflows[workflow_id]))
        current_workflows = next_workflows
    return res


print(get_results(workflows))
