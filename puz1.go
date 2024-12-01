package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"slices"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanLines)
	var l, r int
	ll := make([]int, 0)
	lr := make([]int, 0)

	for scanner.Scan() {
		line := scanner.Text()
		_, err := fmt.Sscanf(line, "%d %d", &l, &r)
		if err != nil {
			panic("failed to parse line")
		}
		ll = append(ll, l)
		lr = append(lr, r)
	}

	slices.Sort(ll)
	slices.Sort(lr)

	counter := make(map[int]int)

	for _, v := range lr {
		counter[v] = counter[v] + 1
	}

	diff := 0
	sim_score := 0

	for idx, v := range ll {
		rv := lr[idx]
		abs := int(math.Abs(float64(rv - v)))
		diff = diff + abs
		sim_score = sim_score + v*counter[v]
	}

	fmt.Println(diff)
	fmt.Println(sim_score)
}
