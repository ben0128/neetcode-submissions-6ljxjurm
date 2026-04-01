class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        const cars = new Array(position.length).fill({})
        cars.forEach((item,idx) => {
            cars[idx] = {
                pos: position[idx],
                time: (target-position[idx]) / speed[idx]
            }
        })
        cars.sort((a,b) => b.pos - a.pos);
        let max = 0, fleet = 0;
        for (let i=0; i<cars.length; i++) {
            if (cars[i].time > max) {
                fleet++;
                max = cars[i].time;
            }
        }

        return fleet
    }
}
