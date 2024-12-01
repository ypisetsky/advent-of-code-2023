from collections import deque
from util import *

LOW = False
HIGH = True

class FlipFlop:
    def __init__(self, line):
        self.name = line[0][1:]
        self.targets = [target.strip(',') for target in line[2:]]
        self.state = LOW

    def get_signals(self, sender, signal, turn):
        if signal == HIGH:
            return []
        else:
            self.state = not self.state
            return [(self.name, self.state, target, turn) for target in self.targets]
        
    def serialize_state(self):
        return self.state
    
    
class Broadcaster:
    def __init__(self, line):
        self.name = 'broadcaster'
        self.targets = [target.strip(',') for target in line[2:]]

    def get_signals(self, sender, signal, turn):
        return [(self.name, signal, target, turn) for target in self.targets]
    
    def serialize_state(self):
        return None

class Conjunction:
    def __init__(self, line):
        self.name = line[0][1:]
        self.targets = [target.strip(',') for target in line[2:]]
        self.state = {}

    def get_signals(self, sender, signal, turn):
        self.state[sender] = signal
        if all(self.state.values()):
            return [(self.name, LOW, target, turn) for target in self.targets]
        else:
            return [(self.name, HIGH, target, turn) for target in self.targets]
        
    def serialize_state(self):
        return None


def parse_line(tokens):
    if tokens[0][0] == '%':
        return FlipFlop(tokens)
    elif tokens[0][0] == '&':
        return Conjunction(tokens)
    elif tokens[0] == 'broadcaster':
        return Broadcaster(tokens)
    
components = {}
for line in tokenedlines("20"):
    component = parse_line(line)
    components[component.name] = component

for name, component in components.items():
    for target in component.targets:
        if len(target) == 1:
            print(component, "WTF")
        if target in components and isinstance(components[target], Conjunction):
            components[target].state[name] = LOW

def push_button(components, scores):
    queue = deque([("button", LOW, "broadcaster")])
    while len(queue) > 0:
        sender, signal, target = queue.popleft()
        scores[signal] += 1
        if target in components:
            queue.extend(components[target].get_signals(sender, signal))
        elif target == 'rx' and signal == LOW:
            raise NameError(target)
    return tuple(component.serialize_state() for component in components.values())

# scores = defaultdict(int)
# for i in range(1000):
#     push_button(components, scores)

# print(scores, scores[LOW] * scores[HIGH])



targetflips = set()
for source in ["rl", "rd", "qb", "nn"]:
#for source in ["qb"]:
    reached = set([source])
    queue = deque([source])
    while len(queue):
        comp = queue.popleft()
        reached.add(comp)
        if comp == 'rx':
            continue
        queue.extend(neighbor for neighbor in components[comp].targets if neighbor not in reached)

    new_components = {key: components[key] for key in reached if key in components}
    new_components["broadcaster"] = components["broadcaster"]
    i = 0
    states = {}
    while True:
        i += 1
        state = tuple(component.serialize_state() for component in new_components.values())
        if state in states:
            break
        states[state] = i
        queue = deque([("button", LOW, "broadcaster", 0)])
        while len(queue) > 0:
            sender, signal, target, queueturn = queue.popleft()
            if target in new_components:
                queue.extend(components[target].get_signals(sender, signal, queueturn + 1))
            if sender == source:
                targetflips.add((i, queueturn, signal))
                # print(f"TARGET {source} turned {signal} on {queueturn} of button press {i}")
                pass
    print(source, sorted(reached), len(states), [flip for flip in targetflips if flip[2] == False])
print(lcm([flip[0] for flip in targetflips]))