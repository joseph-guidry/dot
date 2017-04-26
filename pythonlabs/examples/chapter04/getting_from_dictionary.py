#!/usr/bin/env python3
rewardPoints = {"Bryce":500, "Heather":2000, "Kaylie":750}
points = rewardPoints.get("Bryce")      # returns 500
print("Bryce:", points)
points = rewardPoints.get("Stephanie")  #returns None
print("Stephanie:",points)

# Supplying a different value to return other than None
points = rewardPoints.get("Stephanie", 0)  #returns 0
print("Stephanie:", points)