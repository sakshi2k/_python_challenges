A technology company announced that a new supply of P monitors would soon be available at their store. There were N orders (numbered from 0 to N-1) placed by customers who wanted to buy those monitors. The K-th order has to be delivered to a location at distance D[K] from the store and is for exactly C[K] monitors.

Now the time has come for the monitors to be delivered. The orders will be fulfilled one by one. To minimize the shipping time, it has been decided that the deliveries will be made in order of increasing distance from the store. If there are many customers at the same distance, they can be processed in any order. 

Monitors to more distant customers will be delivered only once all orders to customers closer to the store have already been fulfilled.

What is the maximum total number of orders that can be fulfilled?


Write a function:
function solution(D, C, P);
that, given two arrays of integers D and C, and an integer P, returns the maximum total number of orders that can be fulfilled.

Examples:
1. Given D = [5, 11, 1, 3], C = [6, 1, 3, 2] and P = 7, the function should return 2. The
customers at distances 1 and 3 will have their orders fulfilled and 3 + 2 = 5 monitors will
be delivered.
2. Given D = [10, 15, 1], C = [10, 1, 2] and P = 3, the function should return 1. Only the
order for the customer at distance 1 will be fulfilled. There will not be enough monitors in the store for the customer at distance 10. Therefore, orders for customers at distances 10 and 15 will not be fulfilled.
3. Given D = [11, 18, 1], C = [9, 18, 8] and P = 7, the function should return 0.
4. Given D = [1, 4, 2, 5], C = [4, 9, 2, 3] and P = 19, the function should return 4.


Write an efficient algorithm for the following assumptions:
• N is an integer within the range [1 - 100,000];
• each element of arrays D and C is an integer within the range [1, 1,000,000,000];
• Pis an integer within the range [O.1,000,000,000].