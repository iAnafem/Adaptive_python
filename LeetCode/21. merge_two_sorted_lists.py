"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# The first solution, without classes. l1 and l2 are Lists


def merge_two_lists_1(l1, l2):
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    result = []
    i1 = 0
    i2 = 0
    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] <= l2[i2]:
            result.append(l1[i1])
            i1 += 1
        else:
            result.append(l2[i2])
            i2 += 1

    if i1 == len(l1):
        result.extend(l2[i2:])
    elif i2 == len(l2):
        result.extend(l1[i1:])
    return result


assert merge_two_lists_1([1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4]
assert merge_two_lists_1([], [1, 3, 4]) == [1, 3, 4]
assert merge_two_lists_1([1, 2, 4], []) == [1, 2, 4]
assert merge_two_lists_1([], []) == []


# The second solution, with SingleLinkedList data structure


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SingleLinkedList:
    def __init__(self):
        """constructor to initiate this object"""

        self.head = None
        self.tail = None

    def add_list_item(self, item):
        """add an item at the end of the list"""

        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

    def list_length(self):
        """returns the number of list items"""

        count = 0
        current_node = self.head

        while current_node is not None:
            # increase counter by one
            count = count + 1

            # jump to the linked node
            current_node = current_node.next

        return count

    def output_list(self):
        """outputs the list (the value of the node, actually)"""

        current_node = self.head
        result = []
        while current_node is not None:
            result.append(current_node.val)

            # jump to the linked node
            current_node = current_node.next
        return result


class Solution:
    @staticmethod
    def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        result = ListNode(0)
        pointer = result
        while l1 is not None or l2 is not None:
            if l1 is None or (l2 is not None and l1.val > l2.val):
                pointer.val = l2.val
                l2 = l2.next

            elif l2 is None or (l1 is not None and l2.val >= l1.val):
                pointer.val = l1.val
                l1 = l1.next

            if l1 is not None or l2 is not None:
                pointer.next = ListNode(0)
                pointer = pointer.next

        return result

    def implementation(self, initial_list_1, initial_list_2):
        if len(initial_list_1) == 0:
            return initial_list_2
        elif len(initial_list_2) == 0:
            return initial_list_1
        list_1, list_2, result_list = SingleLinkedList(), SingleLinkedList(), SingleLinkedList()

        for node_1, node_2 in zip(initial_list_1, initial_list_2):
            list_1.add_list_item(node_1)
            list_2.add_list_item(node_2)

        result_tail = self.merge_two_lists(list_1.head, list_2.head)

        while result_tail.next is not None:
            result_list.add_list_item(result_tail)
            result_tail = result_tail.next

        return result_list.output_list()


solution = Solution()

assert solution.implementation([1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4]
assert solution.implementation([], [1, 3, 4]) == [1, 3, 4]
assert solution.implementation([1, 2, 4], []) == [1, 2, 4]
assert solution.implementation([], []) == []

