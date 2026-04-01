// class Node {
//   constructor(val, next = null, random = null) {
//       this.val = val;
//       this.next = next;
//       this.random = random;
//   }
// }

class Solution {
    /**
     * @param {Node} head
     * @return {Node}
     */
    copyRandomList(head) {
        const visited = new Map();
        const loop = (node) => {
            if (!node) return null;

            const newNode = new Node(node.val)
            visited.set(node, newNode)
            newNode.next = loop(node.next);
            newNode.random = visited.get(node.random) || null;
            return newNode;
        }
        return loop(head);
    }
}
