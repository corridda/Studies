package main

import (
	"fmt"
	"unsafe"
)

/* Consider the following Go structures to illustrate poor versus optimal alignment: */

// Poorly aligned struct
type Misaligned struct {
	Age        uint8  // Uses 1 byte, followed by 7 bytes of padding to align the next field
	PassportId uint64 // 8-byte aligned uint64 for the passport ID
	Children   uint16 //2-byte aligned uint16
}

// Well-aligned struct
type Aligned struct {
	Age        uint8  // Starting with 1 byte
	Children   uint16 // Next, 2 bytes; all these combine into a 3-byte sequence
	PassportId uint64 // Finally, an 8-byte aligned uint64 without needing additional padding
}

type PoorlyAlignedPerson struct {
	Active   bool
	Salary   float64
	Age      int32
	Nickname string
}

type WellAlignedPerson struct {
	Salary   float64
	Nickname string
	Age      int32
	Active   bool
}

func main() {
	poorlyAligned := PoorlyAlignedPerson{}
	wellAligned := WellAlignedPerson{}

	fmt.Printf("Size of PoorlyAlignedPerson: %d bytes\n", unsafe.Sizeof(poorlyAligned))
	fmt.Printf("Size of WellAlignedPerson: %d bytes\n\n", unsafe.Sizeof(wellAligned))

	somehowAligned := PoorlyAlignedPerson{
		Active:   true,
		Salary:   100.5,
		Age:      32,
		Nickname: "Nicky",
	}
	fmt.Printf("somehowAligned: %v\n", somehowAligned)
	fmt.Printf("Size of somehowAligned: %d bytes\n", unsafe.Sizeof(somehowAligned))
	fmt.Printf("Size of somehowAligned.Nickname: %d bytes\n\n", unsafe.Sizeof(somehowAligned.Nickname))

	somehowBetterAligned := WellAlignedPerson{
		Active:   false,
		Salary:   200.5,
		Age:      42,
		Nickname: "Benji_894362145983y59thgiuwynhv5934y9tnf",
	}
	fmt.Printf("somehowBetterAligned: %v\n", somehowBetterAligned)
	fmt.Printf("Size of somehowBetterAligned: %d bytes\n", unsafe.Sizeof(somehowBetterAligned))
	fmt.Printf("Size of somehowBetterAligned.Nickname: %d bytes\n", unsafe.Sizeof(somehowBetterAligned.Nickname))
}
