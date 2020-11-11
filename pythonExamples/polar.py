import cmath

a = complex(input().strip())

print(abs(complex(a)), cmath.phase(a), sep='\n')

