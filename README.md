# HW2 

KAUSHICK SURESH 
1002237680 

**Argue selection sort correctness** 


In order to demonstrate that it sorts correctly, we must solve two key issues: 

**Partial Correctness**: The array will undoubtedly be sorted if the method succeeds. 

**Termination**: After a finite number of steps, the algorithm comes to an end.  

**Partial Correctness**: 

The resultant array will be sorted if the method terminates 

**Invariant**: 

The subarray "arr[0:i]" is sorted and holds the array's smallest "i" elements for each iteration of the outer loop. 

**Proof of Partial Correctness**: 

We need to show that the array is sorted after it is finished in order to prove partial correctness. An invariant, or a condition that holds true during the algorithm's execution, is used to do this: 

Invariant: The subarray arr[0:i] (from the array's beginning to position i-1) is sorted at the start of each outer loop iteration, containing the smallest i entries in the array.  

**Proof by Induction**: 

**Base Case**: The subarray arr[0:0] is empty, therefore it can be easily sorted before any iterations (i.e., when i = 0). 

**Inductive Step**

**Assumption**: Assume that the subarray arr[0:k] is sorted and contains the smallest k elements after k iterations (where k < n). 

**Action**: The method finds the smallest element in the unsorted section (arr[k:n]) and assigns it to index k on the k-th iteration. 

**Result**: Following the placement of this smallest element, the smallest k+1 elements are ordered in the subarray arr[0:k+1]. 

By induction, this invariant ensures that after n-1 iterations, the entire array arr[0:n] is  

sorted, as all elements are placed in their correct positions. 

**Termination**:  

**Outer Loop**: Iterates from 0 to n-1, reducing the unsorted section each time, and will terminate after n iterations. 
**Inner Loop**: Runs n-i times per outer loop iteration, decreasing with i, and will end due to the finite array size.  

By ensuring the invariant holds and both loops terminates after processing all elements, Selection Sort is guaranteed to correctly sort the array and complete in a finite number pf operation. 

BenchMark:

System Info:

Operating System: Windows 11

Processor: Intel64 Family 6 Model 186 Stepping 3, GenuineIntel

RAM: 31.70 GB

![Screenshot (2)](https://github.com/user-attachments/assets/cbe40e4a-2b91-41fb-b48d-323e956e192e)

