def canUnlockAll(boxes):
    # Create a set to track unlocked boxes
    unlocked_boxes = set([0])

    # Iterate through the unlocked boxes
    for current_box in unlocked_boxes:
        # Explore the keys in the current box
        for key in boxes[current_box]:
            # Add the box to unlocked set if not already unlocked
            if key < len(boxes) and key not in unlocked_boxes:
                unlocked_boxes.add(key)

    # Check if all boxes have been unlocked
    return len(unlocked_boxes) == len(boxes)
