from Job import JOB
from GanntChart import *
from ReadData import *
from Dispatch_Rule import *
from heap import *
if __name__ == "__main__":
    for num_of_Dispatching_rule in range(1):
        path = './Normalized_data/data_'
        m_path="./Result/result4"+".csv"
        m = open(m_path, 'w')
        # m.write('Dead Line,POH\n')
        num_run_dataset = 1
        num_hours = 6
        # for time in range(1,7) :
        #     sum_pieces = 0
        #     for i in range(1,num_run_dataset+1) :
        #         path2 = path + str(i) + "_300"
        #         J = []
        #         ReadData(path2, J)
        #         pieces, count = Machine_Oriented(J, 60 * time)
        #         print(time * 60 , pieces, count)
        # # for time in range(1, 12):
        # #     sum_pieces = 0
        # #
        # #     for i in range(1, num_run_dataset+1):
        # #         gan = GanntChart()
        # #         path2 = path + str(i) + "_390"
        # #         J = []
        # #         ReadData(path2, J)
        # #
        # #         count = 0
        # #         if num_of_Dispatching_rule==1:
        # #             pieces, count = WP(J, 60 * time)
        # #         elif num_of_Dispatching_rule == 2:
        # #             pieces, count = FCFS(J, 60 * time)
        # #         elif num_of_Dispatching_rule == 3:
        # #             pieces, count =LFJFM(J, 60 * time)
        # #         elif num_of_Dispatching_rule == 4:
        # #             pieces, count = LFJ_FastM(J, 60 * time)
        # #         elif num_of_Dispatching_rule == 5:
        # #             pieces, count,L = NEH(J, 60 * time)
        # #             J=L
        # #         elif num_of_Dispatching_rule == 6 :
        # #             pieces, count = SPT(J,60 * time)
        # #         elif num_of_Dispatching_rule == 7 :
        # #             pieces, count = WP_adjust(J,60 * time)
        # #         print(i,pieces,count)
        #         sum_pieces += pieces
        #         gan = GanntChart()
        #         gan.init(25, int(max(j.starting_time + j.processing_time for k, j in enumerate(J))), 15)
        #         # print([j.starting_time for k, j in enumerate(J)])
        #         for k, j in enumerate(J):
        #             if j.starting_time + j.processing_time < 60 * time:
        #                 gan.AddJob("J" + str(j.index), j.Machine_Assigned, round(j.starting_time), j.processing_time)
        #         gan.SavetoFile("Gannt Chart/data_" + str(time)+"rule"+str(num_of_Dispatching_rule))
        #
        #     sum_pieces /= num_run_dataset
        #     m.write(str(time * 60) + "," + str(sum_pieces) + "\n")
        weights = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],
                   [0.5,0.5,0,0],[0.5,0,0.5,0],[0.5,0,0,0.5],[0,0.5,0.5,0,0],[0,0.5,0,0.5],[0,0,0.5,0.5],
                   [0.34,0.33,0.33,0],[0.34,0.33,0,0.33],[0.34,0,0.33,0.33],[0,0.33,0.34,0.33],
                   [0.25,0.25,0.25,0.25]]
        pieces = [[[None for _ in range(num_run_dataset)] for _ in range(num_hours)] for _ in range(len(weights))]
        """Write first line"""
        m.write("Deadline ,")
        for i in range(len(weights)):
            # print(" ".join(str(x) for x in weights[i]))
            m.write(" ".join(str(x) for x in weights[i]) + ",")
        m.write("\n")
        for n in range(300,501,10) :
            for w in range(len(weights)) :
                for i in range(1, num_run_dataset+1) :
                    path2 = path + str(i) + "_" + str(n)
                    J = []
                    ReadData(path2, J, weights[w])
                    for time in range(1,num_hours+1) :
                        for j in J : j.is_processed = False #reset all jobs
                        pieces[w][time-1][i-1], count = Machine_Oriented(J, 60 * time)

            """Calculate average"""
            sum_pieces = [[None for _ in range(num_hours)] for _ in range(len(weights))]
            for i in range(len(weights)) :
                for j in range(num_hours) :
                    # print(w,i,pieces[w][i])
                    sum_pieces[i][j] = sum(pieces[i][j]) / num_run_dataset



            """Write remaining part"""
            # for i in range(num_hours) :
            #     m.write(str((i+1) * 60) + ",")
            #     for j in range(len(weights)) :
            #         m.write(str(sum_pieces[j][i]) + ",")
            #     m.write("\n")
            # m.write("\n")
            m.write("POH,")
            for j in range(len(weights)) :
                Sum = 0
                for i in range(num_hours) :
                    Sum += sum_pieces[j][i]
                m.write(str(Sum) + ",")
            m.write("\n")


        # for time, piece in enumerate(pieces) :
        #     m.write(str((time+1) * 60) + "," + str(sum(piece) / num_run_dataset) + "\n") #average pieces
        m.close()
