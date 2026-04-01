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
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(l1, l2) {
        let dummy = new ListNode()
        let node = dummy, temp = 0;
        while (l1 || l2 || temp){
            let base = 0
            base = base + (l1?.val || 0) + (l2?.val || 0) + temp
            temp = 0
            if (base >= 10) {
                base -= 10,
                temp = 1
            }
            dummy.val = base
            l1 = l1?.next, l2 = l2?.next
            if (l1 || l2 || temp) dummy.next = new ListNode()
            dummy = dummy.next
        }
        return node;
    }
}
