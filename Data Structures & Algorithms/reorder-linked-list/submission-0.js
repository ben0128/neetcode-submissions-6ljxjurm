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
        let half = head, tail = head.next;
        while (tail && tail.next) {
            half = half.next;
            tail = tail?.next?.next;
        }
        let newTail = half.next;
        half.next = null;
        let [prev, curr, next] = [null, newTail, null];
        while (curr) {
            next = curr.next
            curr.next = prev

            prev = curr;
            curr = next;
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
