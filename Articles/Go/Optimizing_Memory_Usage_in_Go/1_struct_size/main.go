package main

import (
	"fmt"
	"unsafe"
)

type Employee struct {
	IsAdmin bool
	Id      int64
	Age     int32
	Salary  float32
}

func main() {

	var emp Employee

	fmt.Printf("Size of Employee: %d\n", unsafe.Sizeof(emp))
}
