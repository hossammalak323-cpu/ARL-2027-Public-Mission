def monitor_following_distance(distances: list[float], speeds: list[float]) -> tuple[int, float, int]:
    """
    Analyzes following distance compared to safe distance (speed * 0.5).
    
    Args:
        distances (list[float]): Distance to the lead car at each second.
        speeds (list[float]): Speed of our car at each second.
        
    Returns:
        tuple[int, float, int]: (tailgating_seconds, minimum_distance, tailgate_incidents)
            - tailgating_seconds: total seconds distance was < safe distance
            - minimum_distance: absolute closest distance to the lead car (return 0.0 if empty list)
            - tailgate_incidents: number of separate instances the car started tailgating
    """
    tailgating_seconds=0
    tailgate_incidents=0
    previous_tailgating=False
    if distances:
        minimum_distance=min(distances)
    else:
        minimum_distance= 0.0
        
    for i in range(len(distances)):
        safe_distance=speeds[i]*0.5
        is_tailgating= distances[i] < safe_distance
        
        if is_tailgating:
            tailgating_seconds+= 1 
        
        if is_tailgating and not previous_tailgating:
            tailgate_incidents+= 1
        previous_tailgating=is_tailgating

    return tailgating_seconds, minimum_distance, tailgate_incidents
      
        
