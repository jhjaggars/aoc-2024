package main

import (
	"bufio"
	"flag"
	"fmt"
	"math"
	"os"
	"runtime/pprof"
	"sort"
)

var cpuprofile = flag.String("cpuprofile", "", "write a cpu profile to file")
var puzzlefile = flag.String("puzzlefile", "puzzle1-input.txt", "puzzle input file")

func main() {
	flag.Parse()
	if *cpuprofile != "" {
		f, err := os.Create(*cpuprofile)
		if err != nil {
			panic("can't create cpu profile")
		}
		defer f.Close()
		if err := pprof.StartCPUProfile(f); err != nil {
			panic("couldn't start cpu profile")
		}
		defer pprof.StopCPUProfile()
	}
	f, err := os.Open(*puzzlefile)
	if err != nil {
		panic("can't open puzzle input file")
	}
	defer f.Close()
	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)
	var l, r int
	// ll := make([]int, 0)
	// lr := make([]int, 0)
	var ll [1000]int
	var lr [1000]int
	counter := make(map[int]int)
	// var counter [100000]int

	var idx int
	for scanner.Scan() {
		line := scanner.Text()
		_, err := fmt.Sscanf(line, "%d %d", &l, &r)
		if err != nil {
			panic("failed to parse line")
		}
		// ll = append(ll, l)
		// lr = append(lr, r)
		ll[idx] = l
		lr[idx] = r
		counter[r] = counter[r] + 1
		idx = idx + 1
	}

	sort.Ints(ll[0:1000])
	sort.Ints(lr[0:1000])
	// slices.Sort(ll)
	// slices.Sort(lr)

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
