package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if slow == fast {
			return true
		}
	}
	return false
}

/*
func main() {
	head := ListNode{
		Val:  3,
		Next: nil,
	}
	second := ListNode{
		Val:  2,
		Next: nil,
	}
	third := ListNode{
		Val:  0,
		Next: nil,
	}
	tail := ListNode{
		Val:  -4,
		Next: nil,
	}
	head.Next = &second
	second.Next = &third
	third.Next = &tail
	fmt.Println(hasCycle(&head))
}
*/
