class DNA:
    checkList = [0] * 4  # A C G T 별 최소갯수
    myList = [0] * 4  # A C G T 현재 상태
    checkSecret = 0

    def add_char(self, char):
        if char == 'A':
            self.myList[0] += 1
            if self.myList[0] == self.checkList[0]:
                self.checkSecret += 1
        elif char == 'C':
            self.myList[1] += 1
            if self.myList[1] == self.checkList[1]:
                self.checkSecret += 1
        elif char == 'G':
            self.myList[2] += 1
            if self.myList[2] == self.checkList[2]:
                self.checkSecret += 1
        elif char == 'T':
            self.myList[3] += 1
            if self.myList[3] == self.checkList[3]:
                self.checkSecret += 1

    def remove_char(self, char):
        if char == 'A':
            if self.myList[0] == self.checkList[0]:
                self.checkSecret -= 1
            self.myList[0] -= 1
        elif char == 'C':
            if self.myList[1] == self.checkList[1]:
                self.checkSecret -= 1
            self.myList[1] -= 1
        elif char == 'G':
            if self.myList[2] == self.checkList[2]:
                self.checkSecret -= 1
            self.myList[2] -= 1
        elif char == 'T':
            if self.myList[3] == self.checkList[3]:
                self.checkSecret -= 1
            self.myList[3] -= 1

    def get_case_count(self, p_len: int, a_str_data: str):
        # a_list = [char for char in a_str_data]
        a_list = a_str_data
        a_len = len(a_list)
        cnt = 0

        for i in range(4):
            if self.checkList[i] == 0:
                self.checkSecret += 1

        for i in range(p_len):
            self.add_char(a_list[i])

        if self.checkSecret == 4:
            cnt += 1

        for i in range(p_len, a_len):
            j = i - p_len
            self.add_char(a_list[i])
            self.remove_char(a_list[j])
            if self.checkSecret == 4:
                cnt += 1

        return cnt


dna = DNA()
# dna.checkList = [2, 0, 1, 1]
# print(dna.get_case_count(8, 'CCTGGATTG'))
dna.checkList = [1, 0, 0, 1]
print(dna.get_case_count(2, 'GATA'))
