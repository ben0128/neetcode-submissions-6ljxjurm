class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let max = Math.max(...piles);
        console.log('max', max)
        let min = 0;
        while (min < max-1) {
            let time = 0;
            let each = min + Math.floor((max-min)/2);
            console.log('each', each)
            for (let pile of piles) {
                let res = Math.floor(pile/each);
                time += res === 0 ? 1 : 
                    (pile%each === 0) ? res : res+1;
            }
            if (time > h){
                min = each
            } else {
                max = each
            }
        }
        console.log('check max', max)
        return max;
    }
}
