def winner(b, l):
        return ((b[0][0] == l and b[0][1] == l and b[0][2] == l and b[0][3] == l and b[0][4] == l) or
                (b[1][0] == l and b[1][1] == l and b[1][2] == l and b[1][3] == l and b[1][4] == l) or
                (b[2][0] == l and b[2][1] == l and b[2][2] == l and b[2][3] == l and b[2][4] == l) or
                (b[3][0] == l and b[3][1] == l and b[3][2] == l and b[3][3] == l and b[3][4] == l) or
                (b[4][0] == l and b[4][1] == l and b[4][2] == l and b[4][3] == l and b[4][4] == l) or
                (b[0][0] == l and b[1][0] == l and b[2][0] == l and b[3][0] == l and b[4][0] == l) or
                (b[0][1] == l and b[1][1] == l and b[2][1] == l and b[3][1] == l and b[4][1] == l) or
                (b[0][2] == l and b[1][2] == l and b[2][2] == l and b[3][2] == l and b[4][2] == l) or
                (b[0][3] == l and b[1][3] == l and b[2][3] == l and b[3][3] == l and b[4][3] == l) or
                (b[0][4] == l and b[1][4] == l and b[2][4] == l and b[3][4] == l and b[4][4] == l) or
                (b[0][0] == l and b[1][1] == l and b[2][2] == l and b[3][3] == l and b[4][4] == l) or
                (b[0][4] == l and b[1][3] == l and b[2][2] == l and b[3][1] == l and b[4][0] == l))