// Given an array nums of integers, return how many of them contain an even number of digits.

const findNumbers = (nums) => {
    return nums.filter(x => x.toString().length %2 == 0).length;
}