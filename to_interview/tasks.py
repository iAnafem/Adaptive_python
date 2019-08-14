def pairdiffcount3(arr, k):
    result = []
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) == k:
                if [arr[i], arr[j]] not in result:
                    result.append([arr[i], arr[j]])
    return len(result)


assert pairdiffcount3([4, 4, 4, 2, 2], 0) == 2


def pairdiffcount2(arr, k):
    result = []
    return len([result.append([arr[i], arr[j]])
                for i in range(len(arr) - 1)
                for j in range(i + 1, len(arr))
                if abs(arr[i] - arr[j]) == k
                and [arr[i], arr[j]] not in result])


assert pairdiffcount2([4, 4, 4, 2, 2], 0) == 2


def pairdiffcount(arr, k):
    return len(set([(arr[i], arr[j])
                    for i in range(len(arr) - 1)
                    for j in range(i + 1, len(arr))
                    if abs(arr[i] - arr[j]) == k
                    and (arr[i], arr[j])]))


assert pairdiffcount([4, 4, 4, 2, 2], 0) == 2
