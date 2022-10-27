func twoSum(numbers []int, target int) []int {
    var n int = len(numbers)
    var L int = 0
    var R int = n -1
    var h = []int{}
    
    for L < R{
        res := numbers[L] + numbers[R]
        
        if res == target{
            h = append(h, L+1, R+1)
            return h
        } else if res < target{
            L++
        } else if res > target{
            R--
        }
    }
    h = append(h, -1,-1)
    return h
     
}