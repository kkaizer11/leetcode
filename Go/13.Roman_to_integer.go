package main

import (
	"fmt"
	"strings"
)

func romanToInt(s string) int {
	romans := map[uint8]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	s = strings.Replace(s, "CD", "CCCC", -1)
	s = strings.Replace(s, "CM", "DCCCC", -1)
	s = strings.Replace(s, "XL", "XXXX", -1)
	s = strings.Replace(s, "XC", "LXXXX", -1)
	s = strings.Replace(s, "IV", "IIII", -1)
	s = strings.Replace(s, "IX", "VIIII", -1)

	result := 0
	for _, letter := range s {
		result += romans[uint8(letter)]
	}
	return result
}

func main() {
	x := "IV"
	fmt.Println(romanToInt(x))
}
