package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()

	tokens := strings.Split(scanner.Text(), " ")

	fmt.Printf("a = %s\n", tokens[0])
	fmt.Printf("b = %s", tokens[1])
}
