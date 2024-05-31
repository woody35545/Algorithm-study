// 문제:  https://school.programmers.co.kr/learn/courses/30/lessons/181950

package main

import (
	"fmt"
	"strconv"
)

func main() {
	var inputStr string
	var countStr string
	fmt.Scan(&inputStr, &countStr)

	count, _ := strconv.Atoi(countStr)

	for i := 0; i < count; i++ {
		fmt.Print(inputStr)
	}
}
