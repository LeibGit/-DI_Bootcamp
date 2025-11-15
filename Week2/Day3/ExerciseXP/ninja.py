class Temperature:
    def __init__(self, m_unit, temp):
        self.m_unit = m_unit
        self.temp = temp
 
    def calculate_tempurate(self):
        if self.m_unit == "celcius":
            f = (self.temp*9 /5) + 32
            k = (self.temp + 273.15)
            return f"Fahrenhiet: {f} Kelvin: {k}"
        elif self.m_unit == "fahrenhiet":
            c = 5/9*(self.temp -32)
            k = (self.temp - 32)*5/9 + 273.15
            return f"Celcius: {c} Kelvin: {k}"
        else:
            c = self.temp - 273.15
            f = (self.temp - 273.15)*1.8 + 32
            return f"Celcius: {c} Fahrenhiet: {f}"

# Exercise 2
import random

class QuantumParticle():
    def __init__(self, position=0, momentum=0, spin=0):
        self.position = position
        self.momentum = momentum
        self.spin = spin

    def get_position(self):
        self.position = random.randint(1, 10000)
        return self.position
    
    def get_momentum(self):
        self.momentum = random.random()
        return self.momentum

    def get_spin(self):
        self.spin = random.choice((1/2, -1/2))
        return self.spin
    
    def get_disturbance(self):
        list_of_measurments = [self.position, self.momentum, self.spin]
        random_choice = random.choice(list_of_measurments)
        random_change =  random.randint(1, 100)
        print("Quantum interferences!")
        return random_choice - random_change

    def entangle_particles(self, other):
        if not isinstance(other, QuantumParticle):
            print("Can only entangle with another quantum particle.")
        
        if other.spin == self.spin:
            return f"particle one and two are entangled."
        else:
            return f"particles did not entangle."

    
class Email:
    def __init__(self, subject, header):
        self.subject
        self.header
    
    def send_email(self, other):