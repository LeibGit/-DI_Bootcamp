from random import randint, random

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
    """
        used to check if DNA was returning the correct amt of values

        def checker(self):
        count = 0
        for chromo in self.dna:
            count += 1
        return count
    """

class Organism(DNA):
    def __init__(self, values=[], dna=[], environment=0.1):
        super().__init__(values, dna)
        self.environment = environment

    def mutate(self):
        for i, chromo in enumerate(self.dna):
            for j, gene in enumerate(chromo):
                if random() <= self.environment:
                    self.dna[i][j] = 1
        return self.dna

if __name__=='__main__':
    # put test cases here
    test = Organism()
    print(test.generate_gene())
    print(test.generate_chromosome())
    test.generate_dna()
    print(test.mutate())