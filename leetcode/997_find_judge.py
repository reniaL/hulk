# coding=utf-8


def findJudge(N, trust):
    if N == 1:
        return 1 if not trust else -1
    if N == 2:
        return trust[0][1] if len(trust) == 1 else -1

    trust_count = dict()
    excludes = set()
    for t in trust:
        excludes.add(t[0])
        trust_target = t[1]
        if trust_target in trust_count:
            trust_count[trust_target] = trust_count[trust_target] + 1
        else:
            trust_count[trust_target] = 1

    judge = -1
    for key, value in trust_count.items():
        if value == N - 1 and key not in excludes:
            if judge == -1:
                judge = key
            else:
                return -1
    return judge


if __name__ == '__main__':
    print findJudge(1, [])
    print findJudge(1, [[1, 1]])
    print findJudge(2, [])
    print findJudge(2, [[1, 2]])
    print findJudge(2, [[2, 1]])
    print findJudge(3, [[1, 2], [3, 2]])
