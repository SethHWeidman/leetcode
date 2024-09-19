import typing


class Solution:
    def candy(self, ratings: typing.List[int]) -> int:
        # this problem can be solved by handling the cases when the ratings are increasing,
        # decreasing, and constant separately
        #
        # cleverly keeping track of the `peak` of the last upward slope tends to be an unlocking
        # key here in the case of an upward slope, we simply increment `candies` by the length of
        # the upward slope downward slopes are more interesting. We must similarly increase
        # `candies` by the length of the downward slope, and we can do so "in reverse": if we have
        # "3 2" in our `ratings` array, we can first add one candy for the "3", and then when we
        # see the "2" we can simply add two. However, if the length of the downward slope exceeds
        # the height of the last `peak`, we must increment `candies` to reflect that the end of the
        # previous upward slope should have actually had more candies in it than we "added" when we
        # were incrementing `candies` during the upward slope
        #
        # finally, the case when a cell of `ratings` simply has the same value as the previous cell
        # can be handled by resetting `up`, `down`, and `peak`, and incrementing `candies` by one -
        # subsequent increasing or decreasing slopes can be handled by the logic above
        if len(ratings) == 1:
            return 1

        up = 1
        down = 0
        peak = 1
        candies = 1

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:  # increasing slope
                up += 1
                candies += up

                peak += 1
                if up <= peak:
                    peak = up

                down = 0

            elif ratings[i] < ratings[i - 1]:  # increasing slope
                down += 1
                candies += down

                up = 1
                if down >= peak:
                    candies += 1

            else:
                candies += 1
                up = 1
                down = 0
                peak = 1

        return candies


if __name__ == "__main__":
    s = Solution()

    assert s.candy([1, 0, 2]) == 5
    assert s.candy([1, 2, 2]) == 4
    assert s.candy([1, 3, 2, 2, 1]) == 7
    assert s.candy([1, 2, 3, 5, 4, 3, 2, 1, 4, 3, 2, 1]) == 31

    assert (
        s.candy(
            [
                58,
                21,
                72,
                77,
                48,
                9,
                38,
                71,
                68,
                77,
                82,
                47,
                25,
                94,
                89,
                54,
                26,
                54,
                54,
                99,
                64,
                71,
                76,
                63,
                81,
                82,
                60,
                64,
                29,
                51,
                87,
                87,
                72,
                12,
                16,
                20,
                21,
                54,
                43,
                41,
                83,
                77,
                41,
                61,
                72,
                82,
                15,
                50,
                36,
                69,
                49,
                53,
                92,
                77,
                16,
                73,
                12,
                28,
                37,
                41,
                79,
                25,
                80,
                3,
                37,
                48,
                23,
                10,
                55,
                19,
                51,
                38,
                96,
                92,
                99,
                68,
                75,
                14,
                18,
                63,
                35,
                19,
                68,
                28,
                49,
                36,
                53,
                61,
                64,
                91,
                2,
                43,
                68,
                34,
                46,
                57,
                82,
                22,
                67,
                89,
            ]
        )
        == 208
    )

    print("All test cases passed!")
