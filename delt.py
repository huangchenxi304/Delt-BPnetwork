from cmath import sqrt


def delt(learn_factor, input, output):
    # 计算学习之前的网络误差
    error = 0
    for i in output:
        error = error + i ** 2

    error = sqrt(error)
    print('学习之前的网络误差：' + str(error))

    # 设置初始权值
    w = [0 for i in range(len(input[0]))]

    # 开始学习
    error = 0
    for i in range(len(output)):

        # 计算当前实际输出
        real_oupput = 0
        for k in range(len(output)):
            real_oupput = real_oupput + input[i][k] * w[k]
        print('当前实际输出' + str(real_oupput))

        # 训练新权重
        for n in range(len(input[i])):
            delta_Wn = learn_factor * (output[i] - real_oupput) * input[i][n]
            error = error + (output[i] - real_oupput) ** 2
            w[n] = w[n] + delta_Wn

        print(w)

    # 计算新权重下实际输出
    error = 0
    new_output = [0 for i in range(len(input[0]))]
    for i in range(len(input)):
        temp = 0
        for k in range(len(output)):
            temp = temp + input[i][k] * w[k]
        new_output[i] = temp
        error = error + (output[i] - temp) ** 2
    print('新权重下实际输出' + str(new_output))

    # 计算学习之后的网络误差
    print('学习之后的网络误差：' + str(sqrt(error)))


delt(0.5, [[1, 0, -1, 0], [-1, 0, 0, 1], [0, -1, 1, -1], [-1, -1, -1, 0]], [4,9,0,1])
