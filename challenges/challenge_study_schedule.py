def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    count = 0
    for start, end in permanence_period:
        if not isinstance(start, int) or not isinstance(end, int):
            return None
        if start <= target_time <= end:
            count += 1
    return count
