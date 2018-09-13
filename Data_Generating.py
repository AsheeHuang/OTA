import random
from Job import JOB


if __name__ == "__main__":
    R = [0.2, 0.4, 0.6, 0.8, 1.0, 1.25, 1.5, 1.75, 2, 3]
    for i in range(1, 2):
        random.seed(i)
        for j in range(200,501):
            # print(i,j)
            MIN_MAX = [[float('inf'), 0] for _ in range(4)]
            m = open('Normalized_data/data_' + str(i) + "_" + str(j) + ".csv", 'w')
            m2 = open('Normalized_data/data_' + str(i) + "_" + str(j) + "_Mj.csv", 'w')
            m3 = open('Normalized_data/data_' + str(i) + "_" + str(j) + "_Normal.csv", 'w')
            m.write('p,r,w,v,T\n')
            J = []
            sums = 0
            w_lb = random.randint(1, 24)
            w_ub = min(w_lb + random.randint(5, 24), 25)

            m_range = random.sample([i for i in range(2, 16)], 2)
            m_lb = min(m_range)
            m_ub = max(m_range)
            p_mean = random.randint(10,20)
            p_var = random.random() * 10
            for k in range(0, j):
                job = JOB()

                job.Generating_Data(p_range=(p_mean, p_var), w_range = (w_lb,w_ub) , m_range =  (m_lb,m_ub),v_mean = random.random()*1.5)
                # while job.processing_time == 0:
                #     job.processing_time = round(random.gauss(15.94, 4.23), 3)
                sums += job.processing_time
                MIN_MAX[0][0] = min(MIN_MAX[0][0], job.processing_time)
                MIN_MAX[0][1] = max(MIN_MAX[0][1], job.processing_time)

                MIN_MAX[1][0] = min(MIN_MAX[1][0], job.pieces)
                MIN_MAX[1][1] = max(MIN_MAX[1][1], job.pieces)

                MIN_MAX[2][0] = min(MIN_MAX[2][0], job.weight)
                MIN_MAX[2][1] = max(MIN_MAX[2][1], job.weight)

                MIN_MAX[3][0] = min(MIN_MAX[3][0], len(job.Mj))
                MIN_MAX[3][1] = max(MIN_MAX[3][1], len(job.Mj))

                J.append(job)
            R1 = R * int(j / len(R) +1)

            random.shuffle(R1)
            sums /= j
            for c, v in enumerate(J):
                # print(j,c,sums)
                # print(c,len(R1),R1)
                v.set_release_date(c,sums,R1[c])
                m.write(str(v.processing_time) + "," + str(v.release_date) + "," + str(v.pieces) + "," + str(
                    v.weight) + "," + str(v.Temperature) + "\n")
                for item in v.Mj:
                    m2.write(str(item) + ",")
                m2.write("\n")

            for k in range(4):
                m3.write(str(MIN_MAX[k][0]) + "," + str(MIN_MAX[k][1]) + "\n")
