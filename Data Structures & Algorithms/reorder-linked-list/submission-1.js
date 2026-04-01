/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {void}
     */
    reorderList(head) {
        let slow = head, fast = head.next;
        while (fast && fast.next) {
            slow = slow.next;
            fast = fast.next.next;
        }
        let second = slow.next;
        slow.next = null;
        let prev = null;
        while (second) {
            let next = second.next
            second.next = prev
            prev = second;
            second = next;
        }
        let ans = head
        while (head.next) {
            let temp1 = head.next, temp2 = prev.next;
            head.next = prev;
            prev.next = temp1;
            prev = temp2;
            head = temp1;
        }
        if (prev) head.next = prev;
        return ans;
    }
}
