class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos, sped = zip(*sorted(zip(position, speed), reverse=True))
        times = []
        for i in range(len(pos)):
            time = (target - pos[i]) / sped[i]
            if not times or time > times[-1]:
                times.append(time)

        return len(times)