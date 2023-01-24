def func(lists):
    result = 0
    if ( type(lists) != list ):
        print("false")
        return
    for i in lists:
        val = 0
        if (type(i) == str):
            try:
                val = int(i)
            except:
                val = 0
        result = result + val
    print(result)

if __name__ == "__main__":
    lists = ['4', '3', '-2', 'nothing']
    func(lists)