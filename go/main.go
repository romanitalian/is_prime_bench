package main

import (
	"fmt"
	"math"
	"time"
)

func isPrime(num int) bool {
	if num == 2 {
		return true
	}
	if num == 1 || num%2 == 0 {
		return false
	}
	to := int(math.Sqrt(float64(num)))
	for div := 3; div <= to; div += 2 {
		if num%div == 0 {
			return false
		}
	}
	return true
}

func do(N int) {
	for i := 0; i < N; i++ {
		prime := isPrime(i)
		if prime {
			// fmt.Printf("%+v: %+v\n", i, prime)
		}
	}
}

// go build -o is_prime && ./is_prime
// 7.427660718s
func main() {
	st := time.Now()
	// do(20) // 574ns
	do(10_000_000) // 7.427660718s
	fmt.Printf("%+v\n", time.Since(st))
}
