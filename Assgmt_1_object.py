class Search:
    def __init__(self, L1, L2):
        r = L1 + L2
        r = set(r)
        r = list(r)
        self.L = r

    def dev_id_search(self, dev_id):
        dev_list = self.L
        if dev_id in dev_list:
            return 'Dev Id found, Dev Id =' + str(dev_id) + ' Index =' + str(dev_list.index(dev_id))
        elif dev_id > max(dev_list):
            return 'Not found'
        else:
            for i in dev_list:
                if i > dev_id:
                    return 'val = ' + str(i) + ' ind = ' + str(dev_list.index(i))


def main():
    l1 = [1, 3, 5, 16, 8]
    l2 = [6, 5, 9, 4, 13, 12]
    a = Search(l1,l2)
    r = a.dev_id_search(10)
    print(r)


if __name__ == '__main__':
    main()
