"""PS05 Grader."""

import sys

from solution import Set


if __name__ == '__main__':
    name, n = input(), int(input())
    got, want, ops = [None] * n, [None] * n, [None] * n
    ans, sol = set(), Set()
    for i in range(n):
        l = input().split(' ')
        op, v = l[0], int(l[1])
        if l[0] == 'A':
            want[i], got[i] = ans.add(v), sol.add(v)
            ops[i] = f'add({v})'
        elif l[0] == 'R':
            want[i], got[i] = ans.discard(v), sol.remove(v)
            ops[i] = f'remove({v})'
        else:
            want[i], got[i] = v in ans, sol.contains(v)
            ops[i] = f'contains({v})'

    if got != want:
        print(f"\t❌ Test case #{name} failed")
        if n < 50:
            print(f"\t\tOps:\t{ops}")
            print(f"\t\tGot:\t{got}")
            print(f"\t\tWant:\t{want}")
        sys.exit(1)
    print(f"\t✅ Test case accepted #{name}")
