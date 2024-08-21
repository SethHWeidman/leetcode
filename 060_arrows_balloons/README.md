There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons
are represented as a 2D integer array `points` where `points[i] = [xstart, xend]` denotes a balloon
whose **horizontal diameter** stretches between `x_start` and `x_end`. You do not know the exact
y-coordinates of the balloons.

Arrows can be shot up **directly vertically** (in the positive y-direction) from different points
along the x-axis. A balloon with `x_start` and `x_end` is burst by an arrow shot at x if `x_start
<= x <= x_end`. There is **no limit** to the number of arrows that can be shot. A shot arrow keeps
traveling up infinitely, bursting any balloons in its path.

Given the array `points`, return *the **minimum** number of arrows that must be shot to burst all
balloons*.