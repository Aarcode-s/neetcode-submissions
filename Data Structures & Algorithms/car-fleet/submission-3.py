class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for p , s in zip(position , speed):
            time = (target - p)/s
            cars.append((p ,time))

        cars.sort(reverse=True)

        max_time = 0
        fleet = 0

        for p ,time in cars:
            if time > max_time:
                fleet += 1
                max_time = time
        return fleet

