import random
from math import ceil
import numpy as np
class JOB:
    def __init__(self):
        self.processing_time = 0
        self.index = 0
        self.release_date = 0
        self.pieces = 0
        self.weight = 0
        self.Mj = []
        self.Temperature = 0
        self.WP = 0
        self.Machine_Assigned = 0
        self.starting_time = 0
        self.is_processed = False
        #normalized data
        self.processing_time_n = None
        self.pieces_n = None
        self.weight_n = None
        self.Mj_n = None
        #priority of be chosen
        self.priority = None
    def __repr__(self):
        return("Job index : %d \t release date : %d \t processing time : %d "  % (self.index,self.release_date, self.processing_time))

    def Generating_Data(self,p_variance = 4.23, w_range = (5,25) , m_range = (3,20),v_mean = 1):
        # Processing_time

        p = random.gauss(15.94, p_variance)
        self.pieces = random.randint(w_range[0],w_range[1])
        self.processing_time = round(p) if p > 1 else random.randint(1,25)
        # threshold = random.randint(1, 100)
        # if threshold <= 70:
        #     self.processing_time = round(p)
        #     self.pieces = 25
        # else:
        #     self.pieces = w = random.randint(15, 25)
        #     self.processing_time = round((p / 25) * w)

        # Weight
        self.weight = 1+np.random.poisson(v_mean)

        # threshold = random.randint(1, 100)
        # if threshold <= 50:
        #     self.weight = 1
        # elif threshold <= 80:
        #     self.weight = 2
        # elif threshold < 95:
        #     self.weight = 3
        # else:
        #     self.weight = 4

        # Set Mj
        threshold = random.randint(m_range[0], m_range[1])
        data = [i for i in range(1, 26)]
        random.shuffle(data)
        self.Mj = data[:threshold]
        self.Mj.sort()
        # Set temperature
        self.Temperature = random.randint(100, 201)

    def set_release_date(self,index,sums,r):
        self.release_date = round(index / 25 * sums * r)
        # self.release_date = random.randint(0, 1440)
    def transfer_time(self,curr_temp):
        setup = 5 + abs(self.Temperature - curr_temp) * (0.1)
        setup = int(ceil(setup))
        return setup
    # def __lt__(self, other):
    #     return self.processing_time < other.processing_time
