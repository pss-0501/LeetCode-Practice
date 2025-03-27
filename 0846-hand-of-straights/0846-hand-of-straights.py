class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for i in hand:
            count[i] = 1 + count.get(i, 0)

        sorted_keys = sorted(count.keys())

        for key in sorted_keys:
            if count[key] > 0:  # If this card is still available
                start_count = count[key]
                # Check and form a group starting from `key`
                for i in range(key, key + groupSize):
                    if count.get(i, 0) < start_count:
                        return False
                    count[i] -= start_count

        return True