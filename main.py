from Job import JOB
from GanntChart import *
from ReadData import *
from Dispatch_Rule import *
from heap import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from DEA import DEA_analysis
import itertools
def weights_combination(n) :
    weights = []
    for i in range(n) :
        sel = list(itertools.combinations([c for c in range(n)],i+1))
        for s in sel :
            new = [0 for _ in range(n)]
            for k in s :
                new[k] = 1 / len(s)
            weights.append(new)
    return weights
if __name__ == "__main__":

    for num_of_Dispatching_rule in range(1):
        path = './Normalized_data/data_'
        m_path="./Result/result_prob_model"+".csv"
        m = open(m_path, 'w')
        # m.write('Dead Line,POH\n')
        num_run_dataset = 1
        num_hours = 6
        # weights = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],
        #            [0.5,0.5,0,0],[0.5,0,0.5,0],[0.5,0,0,0.5],[0,0.5,0.5,0,0],[0,0.5,0,0.5],[0,0,0.5,0.5],
        #            [0.34,0.33,0.33,0],[0.34,0.33,0,0.33],[0.34,0,0.33,0.33],[0,0.33,0.34,0.33],
        #            [0.25,0.25,0.25,0.25]]
        weights = weights_combination(5)
        pieces = [[[None for _ in range(num_run_dataset)] for _ in range(num_hours)] for _ in range(len(weights))]
        """Write first line"""
        m.write("Deadline ,")
        for i in range(len(weights)):
            # print(" ".join(str(x) for x in weights[i]))
            m.write(" ".join(str(x) for x in weights[i]) + ",")
        m.write("\n")

        for n in range(300,301) :
            total_lateness,total_pieces,total_flow_time = [], [], []
            for w in range(len(weights)) :
                for i in range(1, 2) :
                    path2 = path + str(i) + "_" + str(n)
                    J = []
                    ReadData(path2, J)
                    for time in range(4,5) :
                        for j in J : j.is_processed = False #reset all jobs
                        # pieces[w][time - 1][i - 1], count = prob_model(J, 60 * time,prob = weights[w])
                        # pieces[w][time - 1][i - 1], count = Machine_Oriented(J, 60 * time, weight=weights[w])
                        for j in J: j.is_processed = False
                        l,p,f,c = Machine_Oriented(J, 60 * time, weight=weights[w])
                        print(n,l,p)
                        total_lateness.append(l)
                        total_pieces.append(p)
                        total_flow_time.append(f)


            print(total_lateness)
            input = [] #include tardiness and flow time
            output = [] #include POH
            # print(np.average(total_lateness,axis = 1))
            input.append(total_lateness)
            input.append(total_flow_time)
            output.append(total_pieces,)
            print(output)
            print(input)
            fig = plt.figure()
            ax = fig.add_subplot(111,projection = '3d')

            ax.scatter(total_lateness,total_flow_time,total_pieces, c = 'r')
            plt.show()
            res = DEA_analysis(input,output)
            for idx,val in enumerate(res) :
                print(weights[idx],val)



            # """Calculate average"""
            # sum_pieces = [[None for _ in range(num_hours)] for _ in range(len(weights))]
            # for i in range(len(weights)) :
            #     for j in range(num_hours) :
            #         # print(w,i,pieces[w][i])
            #         sum_pieces[i][j] = sum(pieces[i][j]) / num_run_dataset
            #
            #
            #
            # """Write remaining part"""
            # # for i in range(num_hours) :
            # #     m.write(str((i+1) * 60) + ",")
            # #     for j in range(len(weights)) :
            # #         m.write(str(sum_pieces[j][i]) + ",")
            # #     m.write("\n")
            # # m.write("\n")
            # m.write("POH,")
            # for j in range(len(weights)) :
            #     Sum = 0
            #     for i in range(num_hours) :
            #         Sum += sum_pieces[j][i]
            #     m.write(str(Sum) + ",")
            # m.write("\n")


        # for time, piece in enumerate(pieces) :
        #     m.write(str((time+1) * 60) + "," + str(sum(piece) / num_run_dataset) + "\n") #average pieces
        m.close()
