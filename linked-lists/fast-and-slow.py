# Find the middle of a linked list.

class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)

# Time: O(n)
# Space: O(1)
def middleOfLinkedList(head: Node) -> Node:
    slow, fast = head, head

    # if the list has even number of nodes and you want the "left-side middle"
    # slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Time: O(n)
# Space: O(1)
def hasCycle(head: Node) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # if there is a cycle, the pointers will overlap eventually
        if fast == slow:
            return True
    return False

def main():
    head = Node(1)
    a = Node(2)
    b = Node(3)
    c = Node(4)
    d = Node(5)

    head.next = a
    a.next = b
    b.next = c
    c.next = d

    print(middleOfLinkedList(head))

    print(hasCycle(head)) # false
    d.next = b # create a cycle
    print(hasCycle(head)) # true


if __name__ == "__main__":
    main()