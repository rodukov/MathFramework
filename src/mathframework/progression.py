class progression:
    class Meta:
        description = 'ararithmetic and geometric progressions'
    class arithmetic:
        def get_an(a1, d, n) -> int or float:
            return a1+d*(n-1)
        def get_sum(a1, an, n) -> int or float:
            return ((a1 + an)/2)*n
    class geometric:
        def get_bn(b1, q, n) -> int or float:
            return b1*(q**(n-1))
        def get_sum(b1, q, n) -> int or float:
            return (b1*(q**n - 1))/(q - 1)