package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	totalPrice, _ := strconv.Atoi(scanner.Text())

	scanner.Scan()
	N, _ := strconv.Atoi(scanner.Text())

	var currentTotalPrice int = 0

	for i := 0; i < N; i++ {
		scanner.Scan()
		tokens := strings.Split(scanner.Text(), " ")

		price, _ := strconv.Atoi(tokens[0])
		quantity, _ := strconv.Atoi(tokens[1])

		currentTotalPrice += price * quantity
	}

	if currentTotalPrice == totalPrice {
		fmt.Print("Yes")
	} else {
		fmt.Print("No")
	}
}
