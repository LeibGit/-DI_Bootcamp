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

if __name__=="__main__":

    test1 = Temperature("kelvin", 300)
    print(test1.calculate_tempurate())