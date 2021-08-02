'''
Hi, here's your problem today. This problem was recently asked by Apple:

You are given an array. Each element represents the price of a stock on that particular day.
Calculate and return the maximum profit you can make from buying and selling that stock only once.

For example: [9, 11, 8, 5, 7, 10]

Here, the optimal trade is to buy when the price is 5, and sell when it is 10, so the return value should be 5 (profit = 10 - 5 = 5).
'''

#time complexity: O(n^2)
#space complexity: O(1)
def buy_and_sell(arr):
    max_profit = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] - arr[i] > max_profit:
                max_profit = arr[j] - arr[i]
    return max_profit

#time complexity: O(n)
#space complexity: O(1)
def buy_and_sell_linear(arr):
    max_profit = 0
    min_price = arr[0]
    for price in arr:
        min_price = min(min_price,price)
        compare_profit = price - min_price
        max_profit = max(max_profit,compare_profit)
    return max_profit

if __name__ == '__main__':
    print(buy_and_sell([9, 11, 8, 5, 7, 10]))
    # 5
    print(buy_and_sell_linear([310, 315, 275, 295, 260, 270,290,230,255,250]))
    # 30
    print(buy_and_sell([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))