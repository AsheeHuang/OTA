from Dispatch_Rule import *
from ReadData import *
from random import random,sample,choice

J = []
def sum_pieces(J, weight, hour=6):
    sum = 0
    # print(J)
    for i in range(1, hour + 1):
        for j in J: j.is_processed = False
        sum += Machine_Oriented(J, 60 * i,weight = weight)[0]
    return sum
def generate_weight(weight_num = 4) :
    sum = 0
    weight = [None for _ in range(weight_num)]
    for i in range(weight_num) :
        num = random()
        weight[i] = num
        sum += num
    for i in range(weight_num) :
        weight[i] /= sum
    # print(weights)
    return weight
class GA(object) :
    class chromosome() :
        def __init__(self,weight) :
            self.weight = weight
            self.fitness = None
            self.cal_fitness()
        def cal_fitness(self):
            self.fitness = sum_pieces(J,self.weight)

    def __init__(self,path,population,generation=100,crossover_rate=0.7,mutation_rate=0.2):
        self.population = population
        self.generation = generation
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.chromosomes = []

    def run(self):
        #init population
        for _ in range(self.population) :
            new_chromosome = self.chromosome(generate_weight())
            self.bisect_insert(self.chromosomes,new_chromosome)
            # for i in self.chromosomes :
            #     print(i.fitness, end = ' ')
            # print()
            # print(self.chromosomes[-1].weight)
        for gen in range(self.generation) :
            for c in range(20) :
                parent1,parent2 = sample(self.chromosomes,2)
                child = self.crossover(parent1,parent2)
                if child :
                    if random() < self.mutation_rate :
                        self.mutation(child)
                    self.bisect_insert(self.chromosomes,child)
            self.chromosomes = self.chromosomes[-self.population:]
        print(self.chromosomes[-1].weight,self.chromosomes[-1].fitness)
        return self.chromosomes[-1].weight



    def crossover(self,c1,c2):
        if random() > self.crossover_rate :
            return None
        child_weight = []
        for i in range(len(c1.weight)) :
            child_weight.append((c1.weight[i] + c2.weight[i]) / 2)
        child = self.chromosome(child_weight)
        return child
    def mutation(self,c):
        index = choice([0,1,2,3])
        c.weight[index] = random()
        sum = 0
        for w in c.weight :
            sum += w
        for i in range(len(c.weight)) :
            c.weight[i] /= sum
        c.cal_fitness()
        # print(c.weight)


    def bisect_insert(self,chromosomes,c):
        key = c.fitness
        left = 0
        right = len(chromosomes)-1

        while left <= right :
            pivot = (left + right) // 2
            if chromosomes[pivot].fitness == key :
                chromosomes.insert(pivot,c)
                return
            elif chromosomes[pivot].fitness > key :
                right = pivot - 1
            else :
                left = pivot + 1
        chromosomes.insert(left,c) #left = right after while loop





if __name__ == "__main__" :
    csv_path = './labeled_data.csv'
    f = open(csv_path,'w')
    f.write("data,w_1,w_2,w_3,w_4\n")
    for i in range(300,401,10) :
        path = './Normalized_data/data_1_' + str(i)
        J = []
        ReadData(path,J)
        ga = GA(path,population=50)
        weights = ga.run()
        f.write(str(path) + "," + str(weights[0]) + "," + str(weights[1]) +"," + str(weights[2]) +"," + str(weights[3])+"\n" )
