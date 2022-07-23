import statistics

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(lizt):
    x = [l[1] for l in lizt]
    y = [l[2] for l in lizt]
    return f"{x}\n{y}"


def mean_median(b):
    return statistics.mean(b), statistics.median(b)


def student_total(lizt):
    sum(lizt)


a = enrollment_stats(universities)
print(a)
