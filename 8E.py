class Fibonacci():
    def __iter__(ops):
        ops.a = 1
        ops.b = 0
        return ops
    
    def __next__(ops):
        c = ops.a + ops.b
        ops.b = ops.a
        ops.a=c
        return c

        


fibo = Fibonacci()
iterate = iter(fibo)

i=0
while i<10:
 print(next(iterate))
 i+=1

