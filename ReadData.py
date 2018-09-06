from Job import JOB

# weight = [0.2,0.2,0.5,0.1]
def ReadData(path, J , weight):
    Read = open(path + ".csv", 'r')
    R2 = open(path + '_Mj.csv')
    R3 = open(path + '_Normal.csv')
    MIN_MAX = [[float('inf'), 0] for i in range(4)]
    Read.readline()
    i = 0
    k = 0
    for line in R3.readlines():
        line = line.strip().split(',')
        MIN_MAX[k][0] = float(line[0])
        MIN_MAX[k][1] = float(line[1])
        k += 1
    for line in Read.readlines():
        line = line.strip().split(',')
        j = JOB()
        j.index = i
        i += 1
        j.processing_time = int(line[0])
        j.release_date = int(line[1])
        j.pieces = int(line[2])
        j.weight = int(line[3])
        j.Temperature = int(line[4])
        j.WP = j.pieces * j.weight / j.processing_time

        j.processing_time_n = (j.processing_time - MIN_MAX[0][0]) / (MIN_MAX[0][1] - MIN_MAX[0][0])
        j.pieces_n = (j.pieces - MIN_MAX[1][0]) / (MIN_MAX[1][1] - MIN_MAX[1][0])
        j.weight_n = (j.weight - MIN_MAX[2][0]) / (MIN_MAX[2][1] - MIN_MAX[2][0])


        J.append(j)
    print(path)
    index = 0
    for line in R2.readlines():
        line = line.strip().split(',')
        for item in line:
            if item != '':
                J[index].Mj.append(int(item))
                J[index].Mj_n = (len(J[index].Mj) - MIN_MAX[3][0]) / (MIN_MAX[3][1] - MIN_MAX[3][0])
        #less priority is better
        J[index].priority = cal_priority(J[index].processing_time_n, J[index].pieces_n , J[index].weight_n, J[index].Mj_n, weight)
        # print(J[index].processing_time_n, J[index].pieces_n, J[index].weight_n, J[index].Mj_n, len(J[index].Mj))
        # print(MIN_MAX[3][0],MIN_MAX[3][1])
        index += 1


def cal_priority(p,w,v,m, weight) :
    #less priority is better
    #we want shorter processing time
    #more piece
    #more weight
    #less flexible
    return  p * weight[0] - w * weight[1] - v * weight[2] + m * weight[3]