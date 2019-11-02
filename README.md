# COSC6320-Programming-Assignment-2


## Instructions:

* __'Main_prog02.py'__ contains the algorithms. To run simply uncomment one of the solution calls in __main__. With __'TGen_Out.txt'__ in same directory as __'Main_prog02.py'__ the program outputs the results. __'TGen_Out.txt'__ is randomly generated test case generated from, __'Test_Generator.py'__. To build test cases of variable record and dimension size see __'Test_Generator.py'__ and relevant comments inside. __'Main_prog02.py'__ can also evaluate other test cases, simply replace __'TGen_Out.txt'__ with the name of the test case, and place the custom test case in the same directory.

## Timing

* Python 'Timeit' module was used for evaluating the runtime of the four algorithms presented (two naive C++ translations, and two algorithms that utilize randomization). 

### Instructions to time: 

* Timeit timing is simple and can be done on CLI or by code modifications. Below is an example:

```timeit.timeit('s.NaiveAlg1()', setup='from __main__ import s', number=500)```

Note that the function, or object function call is passed as a string. The 'setup' keyword argument is your current module, in the example above it uses class s from __main__. The 'number' is for how many times to run the function. Higher number used will lead to more accurate program/function timing due to law of large numbers. Useful reference for timeit can be found here: https://docs.python.org/2/library/timeit.html 

## Correctness

* To prove correctness for randomizedAlg3 and 4 we use the following induction hypothesis, checking n records with respect to all other records gives a partial solution of size n. In the base case of the first record, we check if another point is higher in some dimension and if the current point is higher than nother point in some dimension. The base case is trivially true as we compare each record to our current one and make the same evaluation. We can show each of the following loop iterations are true by applying the same analysis, thus proving the induction hypothesis. When we extend the solution to the total size of input records, the interesting points can be identified. 

## Performance

* The best case performance of randomizedAlg4 will be linear O(dn) in the best case if the first record is the only dominant point. This runtime is achieved by using O(1) cost 'remove' for each record that is dominated. However, the worst case of randomizedAlg4 will be O(dn^2) if every single point is an interesting point. There are two primary enhancements made to randomizedAlg4, randomization and a loop/data structure modifcation. For randomization, there are two factors that remove many worst-case inputs, randomizing the input records order and randomizing the order to process the dimensions. Consider the following example, with some number of records, each record has 10 dimensions filled with eight zeros, one increasing number and one decreasing number. By randomizing the order with which we consider dimensions, we will process this test case faster. Another example is an increasing order of records, randomizing the order will allow for quicker filtration of the non-interesting points. For the loop/data structure speedup, if we use a while loop instead of for loops we can knockout non-interesting points and not have to process them again. This allows cases where the first few records are highly interesting to result in a faster runtime.
