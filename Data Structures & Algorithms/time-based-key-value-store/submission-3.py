class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = {timestamp: value}
        else:
            self.time_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        print(timestamp)
        if key not in self.time_map:
            return ""

        if timestamp in self.time_map[key]:
            return self.time_map[key][timestamp]

        timestamp_list = list(self.time_map[key])

        if timestamp_list[0] > timestamp:
            return ""

        low, high = 0, len(timestamp_list) - 1
        res = -1
        print(timestamp_list)
        while low <= high:
            mid = low + (high - low) // 2
            print(mid)

            if timestamp > timestamp_list[mid]:
                res = timestamp_list[mid]
                low = mid + 1
            else:
                high = mid - 1

        return self.time_map[key][res] if res != -1 else ""
