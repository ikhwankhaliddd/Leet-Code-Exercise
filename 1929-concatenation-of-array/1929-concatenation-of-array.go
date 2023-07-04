func getConcatenation(nums []int) []int {
    
//     var ans []int
    
//     for _, v := range nums {
//         ans = append(ans,v)
//     }
    
//     if len(ans) == len(nums) {
//         for _, v := range nums {
//             ans = append(ans,v)
//         }
//     }
    
//     return ans
// }
    
    ans := make([]int, len(nums))
    
    copy(ans, nums)
    
    ans = append(ans,nums...)
    return ans
}