from random import randint

class Gene():
    def __init__(self, gene=None):
        self.gene = gene

    def generate_gene(self):
        """
        Generate a gene with a value of 0 or 1
        """
        i = randint(0,1)
        self.gene = i
        return self.gene
    
class Chromosome(Gene):
    def __init__(self, values=[]):
        self.values = values

    def generate_chromosome(self):
        count = 0
        while count < 10:
            gene = self.generate_gene()
            self.values.append(gene)
            count += 1
        return self.values

class DNA(Chromosome):
    def __init__(self, values=[], dna=[]):
        super().__init__(values)
        self.dna = dna
    
    def generate_dna(self):
        count = 0
        while count < 10:
            val = self.generate_chromosome()
            self.dna.append(val)
            count += 1
        return self.dna

if __name__=='__main__':
    # put test cases here
    test = DNA()
    print(test.generate_gene())
    print(test.generate_chromosome())
    print(test.generate_dna())