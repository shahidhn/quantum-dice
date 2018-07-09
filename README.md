# N-sided quantum die

Inspired by [How to write a quantum program in 10 lines of code](https://medium.com/rigetti/how-to-write-a-quantum-program-in-10-lines-of-code-for-beginners-540224ac6b45) by [Dave Yen](https://medium.com/@davecyen).

Building an N-sided quantum die (where N is some integer power of 2) is simple - where N = 2^k, pass in k qubits to Hadamard gates. The challenge comes when N is not an integer power of 2.

2^k qubits let you represent values between 0 to 2^k - 1 inclusive, and equivalently, 1 to 2^k. Therefore, for any N < 2^k, simply re-roll the die if you get a value between N + 1 and 2^k. Given that each "roll" is indepdendent, doing this does not affect the fairness of the die. To verify this, we can roll the die a large number of times, and see that in the long run, each "side" of the die appears roughly the same number of times.