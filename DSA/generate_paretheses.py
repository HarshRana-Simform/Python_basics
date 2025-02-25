from typing import List

def gen_paren(n :int) -> List[str]:

    stack = []
    res = []

    def backtrack(open_count :int, closed_count :int):

        if (open_count == closed_count == n):
            res.append("".join(stack))
            return 
        
        if (open_count < n):
            stack.append("(")
            backtrack(open_count + 1, closed_count)
            stack.pop()
        
        if (open_count > closed_count):
            stack.append(")")
            backtrack(open_count, closed_count + 1)
            stack.pop()

    backtrack(0,0)

    return res

def main():

    n = int(input("Enter a value: "))
    print(gen_paren(n))

if __name__ == '__main__':
    main()