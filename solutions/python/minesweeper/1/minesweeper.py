def annotate(minefield):
    n = len(minefield)
    if n == 0:
        return []
    m = len(minefield[0])

    result = []

    for i in range(0, n):
        current_row = ""
        if len(minefield[i]) != m:
            raise ValueError("The board is invalid with current input.")
        for j in range(0, m):
            if minefield[i][j] != ' ' and minefield[i][j] != '*':
                raise ValueError("The board is invalid with current input.")
            if minefield[i][j] == '*':
                current_row += '*'
                continue
            
            cnt = 0
            cnt += (i>0 and minefield[i-1][j] == '*')
            cnt += (i>0 and j>0 and minefield[i-1][j-1] == '*')
            cnt += (i>0 and j+1<m and minefield[i-1][j+1] == '*')
            cnt += (j>0 and minefield[i][j-1] == '*')
            cnt += (j+1<m and minefield[i][j+1] == '*')
            cnt += (i+1<n and minefield[i+1][j] == '*')
            cnt += (i+1<n and j>0 and minefield[i+1][j-1] == '*')
            cnt += (i+1<n and j+1<m and minefield[i+1][j+1] == '*')

            if cnt == 0:
                current_row += ' '
                continue

            current_row += chr(ord('0') + cnt)
        result.append(current_row)

    return result
            
