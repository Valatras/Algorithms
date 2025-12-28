running_effect = []

class State:
    def __init__(self, initialValue):
        self._value = initialValue
        # UI changes, needs to be run on every state change
        self.effects = set()
    
    # with property : .value, it's a method, without property : .value() it's a function
    @property # Getter for value
    def value(self):
        if running_effect:
            self.effects.add(running_effect[-1])
        return self._value
    
    @value.setter
    def value(self, newValue):
        self._value = newValue
        for effect in self.effects:
            effect()  # Run all effects when value changes
    
def effect(fn):
    def transformed():
        running_effect.append(transformed)
        fn()
        running_effect.pop()
    transformed()

hp = State(100)
print(hp.value)

@effect
def update_ui():
    print(f"HP updated to: {hp.value}")

@effect
def check_game_over():
    if hp.value <= 0:
        print("Game Over!")

hp.value = 200 # call property.setter