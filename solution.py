def min_days(n, k, ratings):
    """
    Find minimum number of days to solve all problems.
    
    Args:
        n: number of problems
        k: minimum rating difference required
        ratings: list of ratings for each problem
    
    Returns:
        minimum number of days needed
    """
    # For each day, track the rating of the last problem solved on that day
    days = []
    
    # Process problems in order (increasing difficulty)
    for i in range(n):
        current_rating = ratings[i]
        
        # Try to add current problem to an existing day
        placed = False
        for j in range(len(days)):
            # Check if we can add this problem to day j
            # The last problem on day j must have rating differing by at least k
            if abs(days[j] - current_rating) >= k:
                days[j] = current_rating
                placed = True
                break
        
        # If we couldn't place it in any existing day, start a new day
        if not placed:
            days.append(current_rating)
    
    return len(days)


def solve():
    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().split())
        ratings = list(map(int, input().split()))
        
        result = min_days(n, k, ratings)
        print(result)


if __name__ == "__main__":
    solve()